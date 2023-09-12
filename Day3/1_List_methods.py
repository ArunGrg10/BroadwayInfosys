# append()
 vowels= ["a", "e", "u", "i"]
 vowels.append("u")
 print(vowels)

#extend()
a= [1, 2, 3]
b= [4, 5, 6]
result = a.extend(b)
print(result) #None
print(a) # [1, 2,3, 4, 5, 6]

# insert(index, value)
vowels = ["a", "e", "o", "u"]
vowels.insert(2, "i")
print(vowels)

#remove(value)
 a = [1, 2, 3]
 a.remove(1)
 print(a) # [1,3]
 #a.remove(6) its raises error

# pop(index)
vowels= ["a", "e", "i" "o", "u"]

result= vowels.pop(2)
print(vowels)
print(result)

# Pop() method doesn't necessarilly take a parameter. if parameter not provided then last item from the
#list is poped out

# clear()
a= [2,4,5,34]
a.clear()
print(a) #[]

#index(value,start,end)
vowels = []
result = vowels.index("i")
print(result)

a= [1, 2, 4, 5, 3, 6, 2, 7]
result= a.index(2,2)
print(result) #

result = a.index(1, 2, 8)
print(result)

# count()
a = [1, 2, 4, 5,3 ,5 ,5]
print(a.count(3)) #3
print(a.count(1)) #4

#reverse()
a= [2, 1, 10,9,3]
a.reverse()
print(a) #[3,9,10,1,2]