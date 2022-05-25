

import sqlite3 as lite
from sqlite3 import Error
import sqlite3

class SQlite:
    def __init__(self):
        self.db_local = r"C:\Users\shadn\OneDrive\GitHub\BreadStixTrackPytonEdition\bst.sql"
        self.conn = None
        self.get_connection(self.db_local)
        
    def get_connection(self, db_path):
        try:
            self.conn = lite.connect(db_path)
            print("Connection Good")
        except Error as e:
            print(e)
    
    def sqlite_query(self, sqlite):
        rows = []
        try:
            c = self.conn.cursor()
            c.execute(sqlite)
            
            # notes
            columns = [x[0] for x in c.description]
            rows.append(columns)
            c.close()
            while True:
                row = c.fetchone()
                if row == None:
                    break
                rows.append(row)
        except Error as e:
            print(e)
        return rows
        
            
def main():
        sqlite = SQlite()
        
        print("Column names")
        row = sqlite.sqlite_query("Select * From users")
        coul  = row.pop(0)
        
        print("Columns")
        print(coul)
        print("data")
        print(row)
            
if __name__ == "__main__":
        main()