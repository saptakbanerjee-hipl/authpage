import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE Users (user_name TEXT, email TEXT)')
print("Table created successfully");
conn.close()