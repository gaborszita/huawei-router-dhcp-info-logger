#!/usr/bin/env python3

import mysql.connector

db = mysql.connector.connect(
    host="host",
    user="user",
    password="password",
    database="database"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM table1 WHERE name='Jake'")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db.close()