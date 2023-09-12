# JSON stans for Javascript Object Notation
# JSON is a file format with .json extension which is used  to share data and information ober the internet.
# python has a built-in module for json handling
# JSON is similar to python dictionary as it is also written in key-value format. But, keys and values in JSON
# must be enclosed in double-quotes. Singles quote are not allowed.
# integers and float does not require quotes in JSON

# Some examples of JSON data
# {"name": "Arun", "age": 34, "address": "ktm"} # valid JSON
# {'name': 'Arun', 'age': 34, 'address': 'ktm'} # Invalid JSON bbecause of single quote

# [
#    {"name": "Arun", "age": 34, "address": "ktm"},
#    {"name": "Jpn", "age": 45, "address": "pkr"}
# ]  # valid JSON

import json
filename = "student.json"
student = {'name': "Harry", 'age': 34, 'address': 'ktm'}
students = [
    {"name": "Arun", "age": 34, "address": "ktm"},
    {'name': "Jpn", 'age': 45, "address": "chitwan"}
]
with open(filename, "w+") as fp:
    data = json.dumps(students,indent=2)
    fp.write(data)
    fp.seek(0)
    data = json.loads(fp.read())
    print(data)

name = students[1]["name"]
name1 = students[0]["age"]
print(name1)
print(name)
