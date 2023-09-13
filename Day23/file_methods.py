filename = "message.txt"

with open(filename, "w") as fp:
    fp.write("hello world\nI'm Learning Python")


# read()
# seek()
# readline()
# readlines()
# tell()
# writelines()
with open(filename, "r") as fp:
    data = fp.read()
    print(data) # Hello World I'm learnning python

    fp.seek(0) # seek() method changes the cursor of the file
    data  = fp.read(7) # Hello w
    print(data)

    fp.seek(0)
    data = fp.readline() # file pointer jun line ma xa, tei line ko data matra dinxa
    print(data) # hello world

    fp.seek(0)
    data = fp.readlines() # esle chai list ma dinxa
    print(data) # ["hello world", "I'm learning python"]

data = ["Hello World\n", "I'm Learning Python\n", "Python is a high level language"]
with open(filename, 'w') as fp:
    fp.writelines(data)