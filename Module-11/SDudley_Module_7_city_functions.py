# Sean Dudley
# CSD325 - Module 7 Assignment - City Functions
# 4/26/2025

def city_country(city, country, population='', language=''):
 
    if language and population:
        formatted_location_string = f"{city.title()}, {country.title()}, has a population of {population}, where local residents speak {language.title()}"

    elif population:
        formatted_location_string = f"{city.title()}, {country.title()}, has a population of {population}"    

    elif language:
        formatted_location_string = f"{city.title()}, {country.title()}, where local residents speak {language.title()}"

    else:
        formatted_location_string = f"{city.title()}, {country.title()}"

    return formatted_location_string    

# City Parameters
print('Three foreign locations I have traveled to:')
print(city_country('paris', 'france'))
print(city_country('barcelona', 'spain', '' ,'spanish'))
print(city_country('munich', 'germany', 1600000, 'german'))
print(city_country('barcelona', 'spain', 1628000 ))