student = {"name": "Arun", "age": 34, "roll": 2, "address": "chitwan"}
arun= dict(college="KEC", faculty = "BEX", rollno = 73006)
print(arun)
print(student.keys())

for i in student.keys():
    print(i)

#print(student.values())

for j in student.values():
    print(j)

a = dict(sd = "fdf", dfs= 'sdkfj', df = 34)
print(a)

#print(a.items())
for key, value in arun.items():
    print(key)
    print(value)


for key in a.keys():
    print(key)

for value in a.values():
    print(value)

data= list(arun.items())
print(data)
print(data[1])
print(data[1][1])

student_list= [("name","Jon"), ("age", 34), ("address", "KEM")]
# we can convert it into dictionary in two ways
# 1.
student= dict(student_list)
print(student)

# 2.
student = {key: value for key, value in student_list}
print(student)
print(student.items())

lits = list(student.items())
print(lits)
print(lits[2][0])
print(lits[0:2])


print(list(range(0,30,3)))

vowels = ["a", "e", "i", "o", 'u']
print(enumerate(vowels))
data = list(enumerate(vowels))
print(data)

for key, value in enumerate(vowels,start=3):
    print(key,value)
