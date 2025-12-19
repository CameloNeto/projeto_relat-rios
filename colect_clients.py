import sqlite3
import httpx
import asyncio
from keys import DG_TOKEN
from DataBase import DataBase
import json

async def colect_clients():
    urlDG = 'https://gestao.dg.energy/api/v1/entities/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    database = DataBase()

    while urlDG:
        request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
        results = request.json().get("results")
        for client in results:
            print(client)
            database.insert_clients([client.get('id'), client.get('name'), client.get('document_type'), client.get('document'), json.dumps(client.get('emails')), json.dumps([])])
            break
        break

if __name__ == "__main__":
    asyncio.run(colect_clients())