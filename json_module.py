import json

d= {
    "name": "Alkesh","course":"ECE"
}

x=json.dumps(d)   # it converts the dictionary to string which is basically used in json

print(type(x))   # type's is  str because Json only take string type
print(x)

t=json.loads(x)   # it converts the string to dictionary

print(type(t))
print(t)

