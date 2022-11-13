course={
    'php':{'duration':'2 month','fees':10000},
    'java':{'duration':'1 month','fees':15000},
    'python':{'duration':'3 month','fees':12000}
}
print(course)

print(course['php']['fees'])
# for update
course['php']['fees']=5000
print(course['php']['fees'])
print(course)

for a,b in course.items():
    print(a,b)