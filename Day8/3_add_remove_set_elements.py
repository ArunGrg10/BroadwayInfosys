# add()
s= {1, 2, 3}
s.add(4)
print(s)

# update()
s= {1, 2, 3}
s.update([4, 5, 6])
print(s) # {1, 2, 3, 4, 5, 6}

# remove()
s= {1, 2, 3, 4, 5, 6}
s.remove(4)
print(s) # {1, 2, 3, 5, 6}
s.remove(9) # it raises error


# discard()
s= {1, 2, 3, 4, 5, 6}
s.discard(4)
print(s) # {1, 2, 3, 5, 6}
s.discard(9) # It doesn't raise an error.

# pop()
s= {1, 2, 3, 4, 5, 6}
s.pop()
print(s) # randomly pops out any one element from the set

#clear()
s.clear()
print(s) # {}


