
# first method
l=[]
for a in range (1,101):
    l.append(a)

print(l)

# second method

l=[]
l=[m for m in range(1,101)]
print(l)

l=[m for m in range(1,101) if m%2==0] # we should also pass the filter or condition
print(l)

