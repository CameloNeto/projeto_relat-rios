import sqlite3
from pathlib import Path
import os
import json
import paths
class DataBase:
    """Classe para operações do banco de dados (DRY)"""

    def __init__(self, create_db=False):
        try:
            self.path_db = Path("./database/database.db")
            if not create_db:
                if self.path_db.exists() and Path("./database/").exists():
                    self.con = sqlite3.connect(self.path_db)
                    self.cur = self.con.cursor()
                else:
                    raise FileNotFoundError(f"{ "Arquivo não encontrado" if not self.path_db.exists() else ""} | {"O diretório não existe" if not Path("./database/").exists() else ""}")
            else:
                if not self.path_db.parent.exists():
                    os.makedirs(self.path_db.parent)

                self.con = sqlite3.connect(self.path_db)
                self.cur = self.con.cursor()
                with open(paths.clients_CRUD_path().joinpath('create_clients_table.sql'), 'r', encoding="utf-8") as createclients_sql:
                    self.cur.execute(createclients_sql.read())
                    self.con.commit()

        except Exception as error:
            print(error.args)

if __name__ == "__main__":
    database = DataBase(create_db=True)
