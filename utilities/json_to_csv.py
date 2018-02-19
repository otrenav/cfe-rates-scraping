
import json

from pandas import DataFrame


class IberdrolaCFEParser:

    clean_data = []

    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self.json_data = json.load(f)

    def start(self):
        self._parse()

    def _parse(self):
        for i, row in self.json_data.iterrows():
            self.clean_data.append({
                'year': row['year'],
                'month': row['month'],
                'state': row['state'],
                'municipality': row['municipality'],
                'division': row['division'],
                'rate': self._extract_rate(row['table']),
                'description': self._extract_description(row['table']),
                'date': self._extract_date(row['table']),
                'fixed': self._extract_fixed(row['table']),
                'fixed_unit': self._extract_fixed_unit(row['table']),
                'variable': self._extract_variable(row['table']),
                'variable_unit': self._extract_variable_unit(row['table']),
                'distribution': self._extract_distribution(row['table']),
                'distribution_unit': self._extract_distribution_unit(row['table']),
                'capacity': self._extract_capacity(row['table']),
                'capacity_unit': self._extract_capacity_unit(row['table'])
            })

    def _extract_rate(self, text):
        return text.split()[5]

    def _extract_description(self, text):
        return ' '.join(text.split()[5:]).split('$')[0]

    def _extract_date(self, text):
        return text.split()[4]

    def _extract_fixed(self, text):
        pass

    def _extract_fixed_unit(self, text):
        pass

    def _extract_variable(self, text):
        pass

    def _extract_variable_unit(self, text):
        pass

    def _extract_distribution(self, text):
        pass

    def _extract_distribution_unit(self, text):
        pass

    def _extract_capacity(self, text):
        pass


# 'table': 'Tarifa Descripción Cargo Unidades ENE-18\n'
#       'GDMTO Gran demanda en media tensión ordinaria Fijo $/mes 495.59\n'
#       'Variable (Energía) $/kWh 0.878\n'
#       'Distribución $/kW 84.18\n'
#       'Capacidad $/kW 151.80',
