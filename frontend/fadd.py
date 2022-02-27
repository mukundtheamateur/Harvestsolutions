import sqlite3  
  
con = sqlite3.connect("fdetail.db")  
print("Database opened successfully")  
  
con.execute("create table FDetails (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL, phonenumber TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  