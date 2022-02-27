import sqlite3  
  
con = sqlite3.connect("fdetail.db")  
print("Database opened successfully")  
  
con.execute("create table FDetails (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phonenumber TEXT NOT NULL, adharnumber TEXT NOT NULL, area TEXT NOT NULL, cropg TEXT NOT NULL, cropr TEXT NOT NULL, nitrogen TEXT NOT NULL, phosphorous TEXT NOT NULL, pottasium TEXT NOT NULL, ph TEXT NOT NULL, rainfall TEXT NOT NULL, state TEXT NOT NULL, city TEXT NOT NULL, username TEXT NOT NULL, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")  
  
print("Table created successfully")  
  
con.close()  