import sqlite3
from pathlib import Path
import os
import json
import paths
from typing import List, Union
class DataBase:
    """
    Classe que centraliza as principais operações do banco de dado

    args:
        create_db: Em caso de True o banco e o seu diretório serão criados, com essa operação são criadas todas as tabelas segundo os padrões do CRUD no diretorio "sql/"

    Obs: 
        A intenção dessa classe é a centralização das operações do banco então é recomendado que as operações seja feitas por essa classe.

        Quando uma instância dessa classe é criada são criados dois atributos juntos.
            con - conexão com o banco de dados
            cur - cursor do banco
        Com estes atributos são feitas as operações sql. Não alterar estes atributos senão as operações e otimizações serão mais difíceis futuramente.
    """

    def __init__(self, create_db=False):
        
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

    def insert_clients(self, *clients:List[list]):
        """
        Docstring for insert_clients
        
        :param clients: 
            Dados dos clientes que serão adicionados, em formato de lista, podem ser adicionados vários clientes, basta inserir mais de uma lista, cuidado com a quantidade de dados a serem inseridos.
        :type clients: List[list]
        """
        for client in clients:
            self.cur.execute("insert into clients values(?,?,?,?,?,?)",([i for i in client]))
        self.con.commit()

if __name__ == "__main__":
    database = DataBase()
    contacts = [111111111, 111111111]
    database.insert_clients([1, 'nome', 'CPF', '11111111111', 'email@gmail.com', json.dumps(contacts)],[1, 'nome', 'CPF', '11111111111', 'email@gmail.com', json.dumps(contacts)])
