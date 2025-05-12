# Sean Dudley
# CSD325 - Module 9.2 Assignment - API
# 5/10/2025

import json
import requests
from datetime import datetime


# Test Response  # Commented out as both returned same response.
#response = requests.get('http://www.google.com')
#print('++++Test Response++++')
#print(response.status_code)


# Program constants

people_in_space_api = 'http://api.open-notify.org/astros.json'
station_location_api = 'http://api.open-notify.org/iss-now.json'


# HW Test Response
people_response = requests.get(people_in_space_api)
print('++++People_In_Space_Status++++')
print(people_response.status_code)

location_response = requests.get(station_location_api)
print('++++Location_Status++++')
print(location_response.status_code)



def num_people_in_space():
    people_response = requests.get(people_in_space_api)
    if people_response.status_code == 200:
        return people_response.json()
    else:
        return None

    
def get_location():
    location_response = requests.get(station_location_api)
    if location_response.status_code == 200:
        return location_response.json()
    else:
        return None    

def unformatted_data(data, title):
    print(f'++++{title}Unformatted_Data++++')
    print(data)

def formatted_data_people(data):
    print('++++Formatted_data_for_Current_people_in_space++++')
    print(f"Message: {data['message']}")
    print(f"Number of people currently in space: {data['number']}")
    for person in data['people']:
        print(f"{person['name']} on {person['craft']}")
    print()     

def formatted_data_location(data):
    print('++++Formatted_data_for_Current_Station_Location++++')
    print(f"Message: {data['message']}")
    timestamp = datetime.fromtimestamp(data['timestamp'])
    print(f"Timestamp: {timestamp}")
    print(f"Longitude: {data['iss_position']['longitude']}")
    print(f"Latitude: {data['iss_position']['latitude']}")

def main():

    people_in_space_data = num_people_in_space()
    if people_in_space_data:
        unformatted_data(people_in_space_data, "People currently in space.")
        formatted_data_people(people_in_space_data)
    else:
        print('Error getting the number of people currently in space.')
    
    location_data = get_location()
    if location_data:
        unformatted_data(location_data, "Station Location ")
        formatted_data_location(location_data)
    else:
        print('Error getting the location of the ISS station.')

if __name__ == "__main__":
    main()        