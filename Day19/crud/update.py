import json
filename = "students.json"

def update_student(student_id):
    with open(filename, "r+")as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x:x['id'] == student_id), students)
        if student:
            student = student[0] # {"id": 1, "name": 'hary", "age": 23}

            index = students.index(student) # 0

            key = input("enter info you want to update ")
            new_value = input("enter the new value")
            student[key] = new_value # {"id":1, "name": "jane"}
            students[index] = student # student[0] = {"id":1, "name": "jane"}
            fp.seek(0)
            fp.write(json.dumps(student, indent = 2))
            print("student updated successfully")
        else:
            print("invalid student id")


