l=[10,20,31,16,58,10,10]
print("Find no of value present in te list")
m=l.count(10) ## it count no of element 10 present in the list
print(m)
l=["hello","world","hello"]
m= l.count("hello")
print(m)

print(" ")
print("MAX VALUE IN LIST")
l=[10,20,31,16,58,10,10]
m= max(l)  # max fn give the maximum value in the list
print(m)
l=["hello","world","hello"]
m= max(l)
print(m)

print(" ")
print("MIN VALUE IN LIST")
l=[10,20,31,16,58,10,10]
m= min(l)  # min fn give the min value
print(m)
l=["hello","world","hello"]
m= min(l)
print(m)

print(" ")
print("sort the list")
l=[10,20,31,16,58,10,10]

l.sort()  # min fn give the min value
print(l)
l=["hello","world","hello"]
l.sort()
print(l)
print(" ")
print("reverse the list")
l=[10,20,31,16,58,10,10]

l.reverse()  # min fn give the min value
print(l)
l=["hello","world","hello"]
l.reverse()
print(l)


print("index the list")
l=[10,20,31,16,58,10,10]

m=l.index(58)  # min fn give the min value
print(m)
l=["hello","world","hello"]
m=l.index("hello")
print(m)
print("We cannot use find fn in the list it is used for string")
l="hello"
print(l.find('o',0))







