# Sort

a= [(3, 5), (3, 12), (1, 22), (544, 656)]
def get_last_number(data):
    return data[1]

a.sort(key=get_last_number)
##a.sort(reverse=True)
print(a)

b= [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def get_the_last_no(data):
    return data[-1]
b.sort(key=get_the_last_no,reverse=True)
print(b)
b.sort(reverse=True)
print(b)

result= a.extend(b)
print(result)


def add(a,b):
    return a+b

result= add(54,6)
print(result)

a.insert(2, 'dskfj')
result= a.insert(3, "arun")
print(result)
print(a)


