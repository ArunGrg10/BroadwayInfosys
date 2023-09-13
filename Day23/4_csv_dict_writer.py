import csv
students = [
    {"id": "1", "name": "Jon", "age": "39", "address": "KTM"},
    {"id": "2", "name": "erwe", "age": "38", "address": "dffg"},
    {"id": "3", "name": "fdfd", "age": "34", "address": "lkdjf"},
    {"id": "4", "name": "asd", "age": "12", "address": "df"}
]

filename = "students_writer.csv"

with open(filename, "w") as cw:
    field_names = students[0].keys() # ['id', 'name', "age", "address"
    csv_writer = csv.DictWriter(cw, fieldnames=field_names)
    csv_writer.writeheader()
    for student in students:
        csv_writer.writerow(student)