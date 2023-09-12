student = {"name": "Jon", "age": 34}
student1 = student.copy()
print(student) # {"name": "Jon", "age": 34}
print(student1) # {"name": "Jon", "age": 34}

# get()
student = {"name": "Jon", "age": 34}
name = student.get("name")
print(name) # Jon

name = student["name"]
print(name) # Jon

roll = student.get('roll') None
# roll = student['roll'] # error

role = student.get("roll", 5)
print(roll) # 5

name = student.get("name", "Jane")
print(name) # Jon (priority student dictionaty lai nai janxe. yedi dictionary ma bhaena bhane "Jane") print hunxa

# items()
student = {"name": "Jon", "age": 34}
print(student.items()) # dict_items[("name", "Jon"), ("age", 34)]

# keys()
student = {"name": "Jon", "age": 34}
print(student.keys()) # dict_keys(["name", "age"])

# values()
student = {"name": "Jon", "age": 34}
print(student.values()) # dict_keys(["Jon", 34])


