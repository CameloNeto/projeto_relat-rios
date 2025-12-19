import sqlite3
from pathlib import Path
import os
class DataBase:
    """Classe para operações do banco de dados (DRY)"""
    
    def __init__(create_db=False):
        try:
            path_db = Path("./database/database.db")
            if not create_db:
                if path_db.exists() and Path("./database/").exists():
                    con = sqlite3.connect(path_db)
                else:
                    raise FileNotFoundError(f"{ "Arquivo não encontrado" if not path_db else ""} | {"O diretório não existe" if not Path("./database/").exists() else ""}")
            else:
                if not path_db.parent.exists():
                    os.makedirs(path_db.parent)
                
                con = sqlite3.connect(path_db)
                cur = con.execute()
        except Exception as error:
            print(error.args)
        