from pydoc import text
import sqlite3
from uuid import uuid4
import json
import paths
from sqlalchemy import select
from sqlalchemy import text
from models.make_session import db_session
from models.client import client

with db_session() as session:
    search = session.es
    print(search)

