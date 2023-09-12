# dictionary keys has a restriction that they must be immutable datatype
# There is no such restriction in dictionary values

a = {"name": "hana", "age": 34} # valid
b = {1: "hello", 2: "world"} # valid
c = {3.434: "hello", 1.23: "sir"} # valid
d = {(3,4): "hello", (45,6)} # valid
e = {[1,2]: "hello", [5,6]: "world"} # invalid
f = {([3,4]: "ello", [6,6]: "er")} # invalid