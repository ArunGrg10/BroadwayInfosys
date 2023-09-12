import json
filename = "students.json"



def delete_student(student_id):
    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x: x['id'] == student_id, students))
        if student:
            students.remove(student[0])
            with open(filename, "w"):
                fp.write(json.dumps(students, indent=2))
            print("student has been removed succssfuly")
        else:
            print("invalid syntax")
    repeat = input("do you want to continue? y/n: ")
    return True if repeat.lower() == 'y' else False
