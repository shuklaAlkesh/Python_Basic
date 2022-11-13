print("first method to print the two list ")
l=[10,20,30,21]
l1=[25,12,63,24]
l3 =[9,10,15,4]
for a,b,c in zip(l,l1,l3):  # zip function is used to iterate two or more list
    print(a,b,c)
print("second method to print the two list ")
l=[10,20,30,21]
l1=[25,12,63,24]
t = len(l)
for h in range(t):
    print(l[h],l1[h])