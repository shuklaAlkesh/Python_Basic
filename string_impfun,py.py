w= "Welcome123"
print(w.find('2',2)) # it will start from index 2 and then find the character
w= "Welcome123"
print(w.find('t')) # this will give -1 means the characyer is  no present

w= "Welcome123"
print(w.index('e',2)) # it follow same method as find( fun but it will give error if character is not present in string

w= "Welcome123"
# print(w.index('t')) check it will give error if charater is not present instring

w="Welcome"
print(w.isalpha())
w="Welcome123"
print(w.isalpha())

w="123"
print(w.isdigit())
w="Welcome123"
print(w.isdigit())

w="Welcome123"
print(w.isalnum())

w="123"
print(w.isalnum())

w="Welcome"
print(w.isalnum())