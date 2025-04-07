# Sean Dudley
# CSD325 - Module 4 Assignment
# 4/6/2025



import csv
from datetime import datetime

from matplotlib import pyplot as plt



filename = r'C:\Users\seanm\OneDrive\Desktop\School Copies\Bellevue\2025\Needed Files\sitka_weather_2018_simple.csv'


while True:

    # Ask the user if they are looking for the High Temps or the Low Temps
    user_response = input('Would you like to graph the High Temperatures,  the Low temperatures, or would you like to exit? (Please type High, Low or Exit to choose)').upper()

    # Initiate User Input Check

    if user_response == 'EXIT':
        print('Thank you for using this program.')
        break  

    if user_response != 'HIGH' and user_response != 'LOW':
        print('Please check your entry.')
        continue

    # Get dates and  temperatures from file, then process
    dates, temps = [], []

    # Read and process file information
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)


        for row in reader:
            
            try:

                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)

                if user_response == 'HIGH':
                    temp = int(row[5])
                    temps.append(temp)

                elif user_response == 'LOW':
                    temp = int(row[6])
                    temps.append(temp)
                else:
                    break

            except ValueError:
                print(f'Missing information from row: {row}')
                continue     
 
    # Plot the temperatures.

    fig, ax = plt.subplots()

    color = 'red' if user_response == 'HIGH' else 'blue'
    ax.plot(dates, temps, c = color)

    plt.title(f'Daily {user_response} Temperatures - 2018', fontsize=18)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
