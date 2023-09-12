# String index and slicing is similar to that of List
# Forward Indexing starts from 0 ad reversing indexing starts for -1

# String indexing
message = "hello world"
print(message[0]) # H
print(message[3]) # l
print(message[5]) # <space>
print(message[-1]) d
print(message[-7]) # o
print(message[34]) # It raises error; Index Error
print(message[-14]) # It raises error; Index Error

# String slicing
message= "hello world"
print(message[:5]) # "hello"
print(message[0:5]) # "hello"
print(message[3:]) # "lo world"
print(message[2:7]) # "llo w"
print(message[7:2]) # ""

print(message[:-3]) # "hello wo"
print(message[0:-3]) # "hello wo"
print(message[-4:]) # "orld"
print(message[-2:-7]) # ""
print(message[-7:-2]) # "o wor"
print(message[7:-8]) # ""
print(message[-8:7]) # "lo w"
