import sqlite3  
  
con = sqlite3.connect("login.db")  
print("Database opened successfully")  
  
con.execute("create table users (user_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT varchar unique, email TEXT varchar unique, password TEXT NOT NULL, path TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  
