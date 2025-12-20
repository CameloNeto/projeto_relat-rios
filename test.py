import sqlite3
from uuid import uuid4
import json
import paths
from DataBase import DataBase

database = DataBase()

verify = database.cur.execute("SELECT * FROM clients WHERE id = ?", (697,)).fetchone()
if not verify:
    database.insert_clients([697, 'cliente teste',"CPF","","",""])

print(verify)