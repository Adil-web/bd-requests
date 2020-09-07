import requests
import sqlite3

url = "https://jsonplaceholder.typicode.com/todos/1"
r = requests.get(url)
data = r.json()
db = sqlite3.connect('test.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS mytodos (userid INT, title TEXT)""")
db.commit()
userID = data["userId"]
title = data["title"]
sql.execute(f"INSERT INTO mytodos VALUES (?, ?)", (userID, title))
db.commit()

for value in sql.execute("SELECT * FROM mytodos"):
    print(value)

# print(data)
