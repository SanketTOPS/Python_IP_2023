import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connectd!")
except Exception as e:
    print(e)

# Table Created
tbl_create="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

# Insert Data
"""n=int(input("Enter number of records you want:"))

def insertdata():
    name=input("Enter Name:")
    sub=input("Enter Subject:")
    insert_qu=f"insert into studinfo(name,sub) values ('{name}','{sub}')"

    try:
        dbcon.execute(insert_qu)
        dbcon.commit()
        print("Record Inserted!")
    except Exception as e:
        print(e)

for i in range(n):
    insertdata()"""

# Update Records
"""update_qu="update studinfo set sub='angular' where id=4"
try:
    dbcon.execute(update_qu)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

# Delete Records
"""delete_qu="delete from studinfo where id=4"
try:
    dbcon.execute(delete_qu)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""

cur=dbcon.cursor()
# Show Records
select_qu="select * from studinfo"
try:
    cur.execute(select_qu)
    data=cur.fetchall()
    #data=cur.fetchmany(2)
    #data=cur.fetchone()
    #print(data)
    for i in data:
        print(i[2])
except Exception as e:
    print(e)