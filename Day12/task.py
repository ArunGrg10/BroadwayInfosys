# wap to delete all teh occurarences of a specified character in a given string
# s = "All the occurences of a specified character in a given string"
# input = "a"
# output = " ll the occurences of specified chrcter in given string"

#S = str(input("enter the string"))
#for i in S:
 #   if i == "a":
 #       continue

#print(i)

S = "All the occurences of a specified character in a given string"
result = " "
picked_char = input("pick a character")
for each in S:
    if each.lower() == picked_char.lower():
        continue
    result += each

print(result)

# Create a new list of repeated items from a provided list:
# nums = [3,4,2,2,1,3,3,3]
# output = [3,2]

#nums = [3,4,2,2,1,3,3,3]
#result = []
#for num in nums:
 #   if num
  #      print(resul.append(num))

nums = [3,4,2,2,1,3,3,3]
result = []
for each in num:
    if nums.count(each) > 1 and each not in reault:
        result += each

print(result)