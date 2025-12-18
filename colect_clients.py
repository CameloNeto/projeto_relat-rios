import sqlite3

con = sqlite3.connect('./database/database.db')
cur = con.cursor()