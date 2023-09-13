
# CSV stands for Comma Seperated Valudes
# CSV files have extension .csv


# csv is file format in analysing where data can be in commas . fb can downloads all the information in csv

import csv

filename = "students.csv"
with open(filename, "r") as cr:
    #csv_reader = csv.reader(cr)

    for each_line in csv.reader(cr):
        print(each_line)

# Task:
"""[
    {"id": 1, "name": "Jon", "address": "Ktm"},
    {"id": 2, "name": "Jane", "address": "PKR"},
    {"id": 3, "name": "Ken", "address": "BKT"}
]"""

with open(filename, "r") as cr:
    #csv_reader = csv.reader(cr)
    result = []
    for count, each_line in enumerate(csv.reader(cr)):
        if count == 0:
            continue
        data = dict(id=each_line[0], name=each_line[1], age= each_line[2], address=each_line[3])
        result.append(data)

print(result)
