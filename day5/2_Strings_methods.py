# 1. capitalized()
message = "hello world"
result = (message.capitalize())
print(result) # Hello world

# 2. title()
result = message.title()
print(result) #Hello World

# 3. upper()
result = message.upper()
print(result) # HELLO WORLD

# 4. lower()
resut= message.lower()
print(result) # hello world

# 4. split()
message= "hello all. I am learning python"
result = message.split() # calling split() without any parameters. It splits with <space> by default
print(result) # ["hello", "all.", "I", "am", "learning", "python"]

result= message.split("o")
print(result) # ["hell", " all. I am learning pyth", "n"]

message = "Hello,all,I,am,learning,Python"
result =message.split(",")
print(result) #['Hello', 'all', 'I', 'am', 'learning', 'Python']

# join()
info= ['Hello', 'all', 'I', 'am', 'learning', 'Python']
result = " ".join(info)
print(result) # Hello all I am learning Python

# ino.join(" ") # It raises error because join() should be called with string object not with list

result= "+".join(info)
print(result) # Hello+all+I+am+learning+Python


result= ", ".join(info)
print(result) # Hello, all, I, am, learning, Python

# info.join(" ") # It raises error becuse join() should be called with string object not with list

# find()
message = "hello world"
result = message.find('w')
print(result) # 6

result = message.find("rld")
print(result) # 8

result = message.find("Rld")
print(result) # -1 Ifstring is not found then find() returns -1.

search_value= "Rld"
result= message.find(search_value.lower())
print(result)

# replace()
message = "hello world"
result = message.replace("hello", "Hello")
print(result) # Hello world
