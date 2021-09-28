print('THE OVERHEAD WAY TO DO IT ')
with open("weather_data.csv") as data_file:
    days = data_file.readlines()
    print(days)


print('\n PYTHON HAS A BUILT IN CSV MODULE\n')
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

print('\n BUT WE WILL USE PANDAS !\n')

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
temperatures=data["temp"]
print(temperatures)
