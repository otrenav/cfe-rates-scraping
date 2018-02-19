
import os
import time
import pprint
import pandas
import itertools

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from utilities.constants import (
    START_URL, YEARS, YEAR, MONTHS, MONTH, STATES, STATE,
    MUNICIPALITIES, MUNICIPALITY, DIVISIONS, DIVISION, RATE,
    DESCRIPTION, DATE, FIXED, FIXED_UNIT, VARIABLE, VARIABLE_UNIT,
    DISTRIBUTION, DISTRIBUTION_UNIT, CAPACITY, CAPACITY_UNIT,
)


class IberdrolaCFE:

    data = []

    def __init__(self):
        self.driver = SeleniumDriver().driver

    def start(self):
        self._scrape()
        self._save_data()

    def _scrape(self):
        self.driver.get(START_URL)
        self.years = self._extract(YEARS)
        for year in self.years.keys():
            self._scrape_year(year)

    def _scrape_year(self, year):
        self._pause()
        self.year = year
        self._click(YEAR, year)
        self.months = self._extract(MONTHS)
        self.states = self._extract(STATES)
        for c in itertools.product(self.months.keys(), self.states.keys()):
            self._scrape_state(c)

    def _scrape_state(self, comb):
        self._pause()
        self.month, self.state = comb
        self._click(MONTH, self.month)
        self._click(STATE, self.state)
        self.municipalities = self._extract(MUNICIPALITIES)
        for municipality in self.municipalities.keys():
            self._scrape_municipality(municipality)

    def _scrape_municipality(self, municipality):
        self._pause()
        self.municipality = municipality
        self._click(MUNICIPALITY, municipality)
        self.divisions = self._extract(DIVISIONS)
        for division in self.divisions.keys():
            self._scrape_division(division)

    def _scrape_division(self, division):
        self._pause()
        self.division = division
        self._click(DIVISION, division)
        self._add_data()

    def _add_data(self):
        observation = {
            'year': self.years[self.year],
            'month': self.months[self.month],
            'state': self.states[self.state],
            'municipality': self.municipalities[self.municipality],
            'division': self.divisions[self.division],
            'rate': self._extract_text(RATE),
            'description': self._extract_text(DESCRIPTION),
            'date': self._extract_text(DATE),
            'fixed': self._extract_text(FIXED),
            'fixed_unit': self._extract_text(FIXED_UNIT),
            'variable': self._extract_text(VARIABLE),
            'variable_unit': self._extract_text(VARIABLE_UNIT),
            'distribution': self._extract_text(DISTRIBUTION),
            'distribution_unit': self._extract_text(DISTRIBUTION_UNIT),
            'capacity': self._extract_text(CAPACITY),
            'capacity_unit': self._extract_text(CAPACITY_UNIT)
        }
        self.data.append(observation)
        print('-' * 50)
        pprint.pprint(observation)
        print('-' * 50)

    def _save_data(self):
        data = pandas.DataFrame(self.data)
        data.to_csv("./outputs/data.csv", index=False)

    def _click(self, selectors, value):
        success = False
        for s in selectors:
            try:
                self.driver.find_element_by_xpath(s.format(value)).click()
                success = True
                break
            except NoSuchElementException:
                pass
        if not success:
            raise ValueError("{} selectors did not work".format(selectors))

    def _extract(self, selectors):
        success = False
        for selector in selectors:
            try:
                values = self._extract_values(selector)
                texts = self._extract_texts(selector)
                success = True
                break
            except NoSuchElementException:
                pass
        if not success:
            raise ValueError("{} selectors did not work".format(selectors))
        return {
            value: text
            for value, text in zip(values, texts)
            if not (value == "0" or value == 0)
        }

    def _extract_texts(self, selector):
        objects = self._objects(selector)
        return [o.text for o in objects]

    def _extract_values(self, selector):
        objects = self._objects(selector)
        return [o.get_attribute('value') for o in objects]

    def _extract_text(self, selector):
        return self.driver.find_element_by_xpath(selector).text

    def _objects(self, selector):
        return (
            self.driver
            .find_element_by_xpath(selector)
            .find_elements_by_tag_name('option')
        )

    def _pause(self):
        time.sleep(0.5)


class SeleniumDriver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        self._driver = webdriver.Chrome(
            '{}/utilities/chromedriver'.format(
                os.path.dirname(os.path.realpath(__file__))),
            chrome_options=options)
        self._driver.set_page_load_timeout(90)
        self._driver.implicitly_wait(60)

    @property
    def driver(self):
        return self._driver


def main():
    scraper = IberdrolaCFE()
    scraper.start()


if __name__ == '__main__':
    main()
