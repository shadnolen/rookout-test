
import sqlite3
from sqlite3 import Error 


    # Connect to SQLite DB
def create_connection(db):
        conn = None
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as e:
            print(e)
        return conn
    
    # Create tables 
def create_table(conn, create_sql):
        try:
            c = conn.cursor()
            c.execute(create_sql)
        except Error as e:
            print(e)
            
def main_table():
        database = r"C:\Users\shadn\OneDrive\GitHub\BreadStixTrackPytonEdition\bst.sql"
        
        user_table = """CREATE TABLE IF NOT EXISTS users(
            id integer PRIMARY KEY,
            user_name text NOT NULL            
            );"""
            
    
    # Connection to DB
        conn = create_connection(database)
        # Create tables 
        if conn is not None:
            create_table(conn, user_table)
        else:
            print("FIND THAT ERROR")
        
if __name__ == "__main__":
    main_table()
    