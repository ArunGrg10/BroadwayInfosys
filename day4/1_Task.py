# Create a list of first 10 multiple of 3

a= []
for value in range(1, 11):
    a.append(value* 3)
print(a)

a.sort(reverse=True)
print(a)

c=[]
b= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in b:
    i = i*3
    c.append(i)
print(c)

a= [2, 4, 5, 6]
b= [i**3 for i in a]
print(b)

x= [i*12 for i in range(1,11)]
print(x)

b= a.copy()
a.append("alskdjf")
print(b)
print(a)
print(b)

