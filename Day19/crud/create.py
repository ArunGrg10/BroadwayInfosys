import os

filename = "students.json"
import json
def create_student():
    id = input("enter student id: ")
    name = input("enter student name:")
    age = input("enter student age: ")

    student = dict(id=id, name=name, age=age)
    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student])
            fp.write(data)
    else:
        with open(filename, "r+") as fp:
            students = json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            fp.write(json.dumps(students, indent = 2))

    print("student added successfully")
    repeat = input("do you want to coninue y/n: ")
    return True if repeat.lower() == "y" else False


