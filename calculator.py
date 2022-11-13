print('''
    + Add
    - subtract
    * Multiply
    / Divide
''')
a=eval(input("Enter the value1 : "))
b=eval(input("Enter the value2 : "))
opr=input("Enter the operator (+,-,*,/ :-")

if opr == "+":
    print(a+b)
elif opr == "-":
    print(a-b)
elif opr == "*":
    print(a*b)
elif opr == "/":
    print(a/b)
else:
    print("invalid operation")
