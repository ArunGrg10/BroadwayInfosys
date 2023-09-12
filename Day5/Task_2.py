sagar = "I am not interested in learning python"
for each in sagar[5:14]:
    print(each)


print(sagar)
print(len(sagar))
print(type(sagar))
print("g" in sagar)
print("t" not in sagar)
arun= "I should learn java"
print(sagar + arun)
print(sagar[3:4])
print(arun.capitalize())
print(arun.upper())
print(arun.lower())
print(arun.title())

result = arun.split()
print(result)

result = arun.split(",")
print(result)

x= ['hello', 'I', 'am', 'Arun']
result = " ".join(arun)
print(result)


print(sagar.split("n"))

message= " Hello all, I'am new to this class"
result= message.split(",")
print(result)

result = ",".join(message)
print(result)

result = "+".join(x)
print(result)

d = arun.find("Ar")
print(d)

value = "Lea"
result = arun.lower().find(value.lower())
print(result)

result = arun.lower().replace("i", "Hi")
print(result)
result = arun.capitalize().replace("Hi", "I")
p = f"I want to be a programmer. {result}"
print(p)




