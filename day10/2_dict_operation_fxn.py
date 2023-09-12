# Membership operation
# Dictionary membership is checked in keys and not in values
student = {"name": "Jon", "age": 34}

print("jon" in student) # False
print("name" in student) # True
print("age" not in student) # False

###### Built-in function ####
student = {"name": "jone", "age": 34}

# len()
print(len(student)) # 2

# sorted()
result = sorted(student)
print(result) # ["age", "name"]

# str()
result = str(student)
print(result) # "{"name": "jone", "age": 34}"

# all(sequence)
# all() function takes only one parameter and that should be an iterable
# all the elements inside the iterable must be truthy for all() to return True

data_list = [1, "hello", [2,3]]
result = all(data_list)
print(result) # True

result = all ([2, 4, 0])
print(result) # False Since 0 is false

# But there is one one exception in all()
result = all([])
print(result) # True

# any(sequence)
# any() function also takes only one parameter and that should be an iterable
# any one element inside the iterable should be truthy for any() to return True

result = any([2, 5,0, False])
print(result) # True

result = any([0, []])
print(result) # False







