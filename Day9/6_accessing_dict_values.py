# Accessing elements of dictionary is similar to that of list. In list we put numbetrs for indexing and in
# dictionary we put "keys" for indexing

student = {"name": "Jane", "age": 34, "address": "KTM"}
name=student["name"]
print(name) # Jane

age = student["age"]
print(age) # 34

address = student["address"]
print(address) # KTM

# phone = student["phone:] # keyError

# We can also access dictionary values using get() method
name = student.get("name")
print(name) # Jane

phone = student.get("phone") # It doesn't raise error. It gives none

# Adding a key-value pair in dictionary
student= {"name": "Jane", "age": 34, "address": "KTM"}
student["phone"] = "098097809809"
print(student) # "name": "Jane", "age": 34, "address": "KTM", "phone": "098097809809"

other_info = {"email": "a@se.com", "roll": 23}
student.update(other_info)
print(student) # "name": "Jane", "age": 34, "address": "KTM", "phone": "098097809809", "email": "a@se.com", "roll": 23

student["name"] = "Arun"
print(student) # "name": "Arun", "age": 34, "address": "KTM", "phone": "098097809809", "email": "a@se.com", "roll": 23


# Removing key-value pair from a dictionary
student = {"name": "Jane", "age": 34, "address": "KTM", "phone": "098097809809", "email": "a@se.com", "roll": 23}
email= student.pop("email")
print(student) # "name": "Jane", "age": 34, "address": "KTM", "phone": "098097809809", "roll": 23
print(email) # a@se.com

#institution = student.pop("institution") # it raises keyError
institution = student.pop("institution", 'Broadway')
print(institution) # Broadway

# popitem()
student= {"name": "Jane", "age": 34, "address": "KTM", "phone": "098097809809", "email": "a@se.com", "roll": 23}