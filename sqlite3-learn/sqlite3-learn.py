#sqlite3-learn.py
#to learn more goto link https://docs.python.org/2/library/sqlite3.html?winzoom=1
'''
call function connect()
call method cursor()
call method execute()
call method commit()
call method close()

'''


import sqlite3

conn = sqlite3.connect('dadabase.db')  
curs = conn.cursor()
try:
    curs.execute("""create table addrbook (id int primary key,name text,age int,phone text)""")
except sqlite3.OperationalError:
    pass

while True:
    cmd = input("input cmd:")
    if cmd == "quit":
        break
    elif cmd == 'store':
        lis = []
        lis.append(int(input("input id:")))
        lis.append(input("input name:"))
        lis.append(int(input("input age:")))
        lis.append(input("input phone:"))
        curs.execute(quary,lis)
        conn.commit()
    elif cmd == 'lookup': 
        quary = "select * from addrbook " + str(input('input select conditions:(eg:where name="lisi")'))
        curs.execute(quary)
        print(curs.description)

conn.close()
