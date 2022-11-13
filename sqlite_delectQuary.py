import sqlite3

conn = sqlite3.connect("sqlite.db")
st_id = input("Enter the student id to delete :--")
conn.execute("DELETE FROM student where st_id=" + st_id)
print("Student data successfully deleted")
conn.commit()
conn.close()
