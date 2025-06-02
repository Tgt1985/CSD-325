# Sean Dudley
# CSD325 - Module 7 Assignment - test_cities
# 4/26/2025

import unittest
from SDudley_Module_7_city_functions import city_country

class City_Test(unittest.TestCase):
    def test_city_country(self):

        #City, Country
        formatted_name = city_country('paris', 'france')
        self.assertEqual(formatted_name, 'Paris, France')

        # City, Country, Population
        formatted_name = city_country('munich', 'germany', '1600000')
        self.assertEqual(formatted_name, 'Munich, Germany, has a population of 1600000')

        # City, Country, Language
        formatted_name = city_country('barcelona', 'Spain', language='spanish')
        self.assertEqual(formatted_name, 'Barcelona, Spain, where local residents speak Spanish')

        # City, Country, Population, Language
        formatted_name = city_country('munich', 'germany', '1600000', language='german')
        self.assertEqual(formatted_name, 'Munich, Germany, has a population of 1600000, where local residents speak German')        
       

if __name__ == '__main__':
    unittest.main()        