# WAP which takes radius as an input and calculate teh area of the circle.
# Pi*r**2

r = float(input("enter radius = "))
Pi = 3.14
Area = Pi * r**2
print(f"{Area} is the area of the circle")


# WAP to find the frequency of the input number in a list
# [5,2,3,5,3,2,3,3,1,4]
a = [5,2,3,5,3,2,3,3,1,4]
num = int(input("enter a number = "))
print(a.count(num))




# WAP which takes radius as an input and calculate the circunferance of the circle
r = int(input("enter the radius of circle = "))
Pi = 3.14
Circ = 2*Pi*r
print(f"the circumference of the circle is {Circ} ")


# Take l and b as an input and find area fo a rectangle
l = int(input(" the length of a rectangle is = "))
b = int(input(" the breadth of a rectangle is = "))
area = l*b
print(f"the area of a rectangle is {area} meter square")


numbers = input("enter numbers: ")
num1, num2, num3 = tuple(numbers.split(","))
print(num1)
print(num2)
print(num3)

## WAP to input a number and check whether the number is odd or even.

a = int(input("enter a random number = "))
if a%2 == 0:
    print("the number is even")
else:
    print("the number is odd")




