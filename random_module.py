import random

print(random.randint(5,10))  # it gives any random integer between two integer

print(random.randrange(5,10))   # it also give integer value between two number but it does not return last value like (3,9) so it return value between 3to 8 but
                                # it doesnot return 9

#l=[10,20,25,36]
l=(10,20,25,16)

print(random.choice(l))  # itb choose any random value in the list or any tupple but not distionary element


r=random.random()  # it returns any value between 0 and 1
print(r)

l=[10,20,25,16]

random.shuffle(l)  # shuffle function is used to suffled the value present in the list not for tupple
print(l)


u= random.uniform(3,9)   # it also any  gives the randon value between 3 and 9
print(u)



