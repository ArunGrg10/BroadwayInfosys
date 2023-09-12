# We can loop (for loop) through the list in teh following way:

a= [1,2,3,4]
b= [] # or b=list()
for i in a:
    x= i**2

    b.append(x)
print(a)
print(b)

b= [i**2 for in a] # this is list comprehension
print(b)

x= [1,2,3,4,5,6,7,8,9,10]
y= []
for i in x:
    i = i*3
    y.append(i)
print(y)