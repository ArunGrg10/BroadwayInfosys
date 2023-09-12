filename = "students.json"
import json
def create_student():
    id = input("enter student id: ")
    name = input("enter student name:")
    age = input("enter student age: ")

    student = dict(id=id, name=name, age=age)
    with open(filename, "w") as fp:
        data = json.dumps(student)
        fp.write(data)
    print("student added successfully")

