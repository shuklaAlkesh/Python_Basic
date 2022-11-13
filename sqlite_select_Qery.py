import sqlite3

conn = sqlite3.connect("sqlite.db")
data = conn.execute("SELECT * FROM student")
for a in data:
    print(a[0],a[1],a[2],a[3])

print("use of limit only first two deta is selected")
data = conn.execute("SELECT * FROM student limit 2,4")
for a in data:
    print(a)

print("searching method")
st_name=input("Enter the name for searing in data :-")
data = conn.execute("SELECT * FROM student where st_name='"+st_name+"'")
for a in data:
    print(a)

print("searching  using first or last letter of name method")
st_name=input("Enter the name for searing in data :-")
data = conn.execute("SELECT * FROM student where st_name like '%"+st_name+"%'")
for a in data:
    print(a)

conn.close()

