#!/usr/bin/env python3

import mysql.connector
import config

db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USERNAME,
    password=config.DB_PASSWORD,
    database=config.DB_DATABASE
)

cursor = db.cursor()

cursor.execute("SELECT * FROM table1 WHERE name='Jake'")
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db.close()