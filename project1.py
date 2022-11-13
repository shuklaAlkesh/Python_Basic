import random

CNUMBER = random.randrange(1,101)
userinput = int(input("Enter the value :--> "))

if userinput > CNUMBER:
    print(CNUMBER)
    print("Your guess value is too high")
elif userinput < CNUMBER:
    print(CNUMBER)
    print("Your guess value is too low")
else:
    print(CNUMBER)
    print("your guess value is equal you win the game ")
