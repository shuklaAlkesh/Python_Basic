d={
    'course' : 'python',
    'fees' : 2000,
    'Name' : 'Alkesh'

}
print("get function")
print(d.get("fees"))
print(" ")
print("keys function")
for a in d.keys():
    print(a)

print(" ")
print("values function")
for a in d.values():
    print(a)

print(" ")
print("items function")
for a,b in d.items():
    print(a,b)

print(" ")
print("del function")
del d['fees']
print(d)

print(" ")
print("pop function")
p=d.pop('course')
print(p)
print(d)

print(" ")
print("update function")
d.update({'Name': 'Alkesh shukla'})
print(d)

print(" ")
print("we also use dict function to create a dictionary ")
print(" ")
print("clear function")
d.clear()
print(d)
d1=dict(name="Alkesh",salary=200000)
print(d1)