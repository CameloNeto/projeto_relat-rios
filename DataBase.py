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

    def verify_number_data(self, data:Union[str, int, list]) -> int:
        """
        Verificar se o dado é um número, caso não seja retorna uma string vazia
        """
        if type(data) == int:
            return data
        
        elif type(data) == list:
            data:list
            verified_list = []
            for i in data:
                if type(i) == int:
                    verified_list.append(i)
                elif type(i) == str:
                    try:
                        int(i)
                        verified_list.append(i)
                    except:
                        verified_list.append("")
            return verified_list
        
        elif type(data) == str:
            try:
                int(data)
                return data
            except:
                return ""

    def insert_clients(self, *clients:List[list], just_numbers:bool=False) -> None:
        """
        Docstring for insert_clients
        
        :param clients: 
            Dados dos clientes que serão adicionados, em formato de lista, podem ser adicionados vários clientes, basta inserir mais de uma lista, cuidado com a quantidade de dados a serem inseridos.
        :type clients: List[list]
        """
        for client in clients:
            data = [self.verify_number_data(i) for i in client]
            f = ""
            count = 0
            for i in data:
                count += 1
                if count == len(data):
                    f += "?"
                else:
                    f += "?,"

            self.cur.execute(f"insert into clients values({f})",(data))
        self.con.commit()

    def exists(self, table:str, column:str, value:Union[str,int]) -> bool:
        """
        Docstring for exists

        :param table: Nome da tabela onde será feita a verificação
        :type table: str

        :param column: Nome da coluna onde será feita a verificação
        :type column: str

        :param value: Valor que será verificado
        :type value: Union[str,int]

        :return: Retorna True se o valor existir na tabela e coluna especificada, caso contrário retorna False
        :rtype: bool
        """
        verify = self.cur.execute(f"SELECT 1 FROM {table} WHERE {column} = ?", (value,)).fetchone()
        if verify:
            return True
        return False

if __name__ == "__main__":
    database = DataBase(create_db=True)
