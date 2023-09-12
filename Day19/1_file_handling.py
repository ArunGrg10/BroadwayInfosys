# We can open, read, write or perform any other kind of work with file using Python.
# There are several modes from which we can open a file.

# r => read file
# w => write in the file
# r+ => read and write mode
# w+ => write and read mode
# a => append mode
# x => exclusive write mode
# a+ => append and read mode


filename = "message.txt"
fp = open(filename, "w")
fp.write("hello world")
fp.close()

fp = open(filename, "r")
data = fp.read()
print(data)
print(type(data)) # string
fp.close()

# closing a file is important as it protects the system from memory leakage
# but sometimes we may forget to close the file
# so, it is better to open a file with context manager

with open(filename, "a") as fp:  # context manager
    fp.write("\nI'm learning python language")

with open(filename, "r+") as fp:
    data = fp.read()
    fp.seek(0) #  it puts the file pointer to the top of the file
    fp.write("Python is a high level language")

with open(filename, "w+") as fp:
    fp.write("I'm learning python")
    fp.seek(0)
    data = fp.read()
    print(data)

with open(filename, "x") as fp:
    fp.write("hello world. I'm learning python.")