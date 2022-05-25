

import sqlite3
conn = sqlite3.connect("userDB.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user(user_id n(5), user_name char(30));")

user_id = input('User ID: ')
user_name = input('User Name: ')

cursor.execute(""" 
               INSERT INTO user(user_id, user_name)
               VALUES(?,?)""", (user_id, user_name))

conn.commit()
print ("it worked")
print(cursor.fetchall())
conn.close()
if(conn):
    conn.close()
    
    print("\n SQL closed.")

