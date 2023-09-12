#Greatest among three numbers

a = input("enter 1st number")
b = input("enter 2nd number")
c = input("enter 3rd number")




if a > b and a > c:
    print(f"{a} is the greatest ")

elif b>c and b>a:
    print(f"{b} is the greastest")

else:
    print(f"{c} is the greatest")




# task 2 WAP to prompt the user for hours and rate per hour usig input to compute gross pay. pay the hourly rate for
# for the hours up to 40 and 1.5 times the hour rate for all hours worked above 40 hours. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to
# convert the string to a number.

hour = int(input("enter the number worked hours"))
rate = float(input("hourly rate "))
total_pay = 0
if hour <= 40:
   total_pay = hour * rate

else:
    overtime = hour - 40
    normal_pay = 40 * rate
    extra_pay = overtime * rate * 1.5
    total_pay = normal_pay + extra_pay

print(f"{total_pay} is the total gross pay")





