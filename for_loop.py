range(1,6)
for n in range(1,10,2):
    print(n)
a=int(input("Enter the value to print table : "))
for i in range(1,11):
    print(a," * ",i," = ",a*i)

a=int(input("Enter the value to print table : "))
for i in range(10,0,-1): # -1 is usd to decrement
    print(a," * ",i," = ",a*i)
