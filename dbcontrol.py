# _*_coding: utf-8 _*_

"""
This script is about what to do with data in PostgreSQL. It receives and saves data from Main.py (user_id and requests).
Later it receives  ready-for-user-data from checker.py and keeps it in DB.
Even later it gives a ready-for-user-data to a main.py back on request.

"""

import psycopg2

conn = psycopg2.connect("dbname = 'botdb' user = 'userbotdb' password = 'botpassword'") #сonnects to DB
cur = conn.cursor() #makes a cursor for operating in DB


try:
    conn
except:
    print('unable to connect')


cur.execute("INSERT INTO botdb (id, user_id, request VALUES (%s, %s, %s)", ()
, (), а , (value1, value2, value3)

n = Main.x