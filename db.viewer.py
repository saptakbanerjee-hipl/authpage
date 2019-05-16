import sqlite3
db = sqlite3.connect('database.db')
cursor = db.cursor()
cursor.execute("SELECT User where user_name= 'Saptak'")
user_data = cursor.fetchone()
print(user_data[0])