import sqlite3
from uuid import uuid4
import json

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
con.commit()