
START_URL = (
    'http://app.cfe.gob.mx/' +
    'Aplicaciones/CCFE/Tarifas/' +
    'TarifasCRENegocio/Tarifas/GranDemandaMTO.aspx'
)
YEARS = [
    '//*[@id="ContentPlaceHolder1_Fecha_ddAnio"]'
]
MONTHS = [
    '//*[@id="ContentPlaceHolder1_Fecha2_ddMes"]',
    '//*[@id="ContentPlaceHolder1_MesVerano2_ddMesCREDic"]'
]
STATES = [
    '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddEstado"]'
]
MUNICIPALITIES = [
    '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddMunicipio"]'
]
DIVISIONS = [
    '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddDivision"]'
]
YEAR = [
    (
        '//*[@id="ContentPlaceHolder1_Fecha_ddAnio"]' +
        '/option[contains(@value, "{}")]'
    )
]
MONTH = [
    (
        '//*[@id="ContentPlaceHolder1_Fecha2_ddMes"]' +
        '/option[contains(@value, "{}")]'
    ),
    (
        '//*[@id="ContentPlaceHolder1_MesVerano2_ddMesCREDic"]' +
        '/option[contains(@value, "{}")]'
    )
]
STATE = [
    (
        '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddEstado"]' +
        '/option[contains(@value, "{}")]'
    )
]
MUNICIPALITY = [
    (
        '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddMunicipio"]' +
        '/option[contains(@value, "{}")]'
    )
]
DIVISION = [
    (
        '//*[@id="ContentPlaceHolder1_EdoMpoDiv_ddDivision"]' +
        '/option[contains(@value, "{}")]'
    )
]

RATE = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[2]/th[1]'
)
DESCRIPTION = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[2]/th[2]'
)
DATE = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[1]/th[5]'
)
FIXED = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[3]'
)
FIXED_UNIT = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]'
)
VARIABLE = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[3]'
)
VARIABLE_UNIT = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]'
)
DISTRIBUTION = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[3]'
)
DISTRIBUTION_UNIT = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[4]/td[2]'
)
CAPACITY = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[3]'
)
CAPACITY_UNIT = (
    '//*[@id="Principal"]/div/div[2]/table[1]/tbody/tr[8]' +
    '/td/table/tbody/tr[1]/td/table/tbody/tr[5]/td[2]'
)
