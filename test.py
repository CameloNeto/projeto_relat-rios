import sqlite3
from uuid import uuid4
import json
import paths

with open(paths.clients_CRUD_path().joinpath("create_clients_table.sql"), 'r', encoding="utf-8") as sql_op:
    print(sql_op.read())