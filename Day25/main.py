# working with csv files and analyzing data with pandas
# Pandas -- biblioteka do analizowania danych
# https://pandas.pydata.org/docs/
import math
from typing import Match

#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
# jest to dość niewygodne rozwiązanie

#import csv
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    print(data)
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(row[1])
#       print(row)

#   print(temperatures)

# ten sposób  wymagad dużo kodu przy złożonych operacjach

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])

#data_dict = data.to_dict()
#print(data_dict)

#temp_list = data["temp"].to_list()

#temp_sum = 0
#for temp in temp_list:
#    temp_sum += temp
# albo używajac sum()
#average_temp = math.ceil(temp_sum / len(temp_list))

#print(data["temp"].mean())
#print(data["temp"].max())

#get data in columns
# trzeba zdefinioować kolumne

#print(data["condition"])
#print(data.condition)

# czytanie wierszy
#print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Tom"],
    "scores": [76,56,65]
}
data_students = pandas.DataFrame(data_dict)
# print(data_students)
data_students.to_csv("new_data_students")