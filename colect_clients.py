import sqlite3
import httpx
import asyncio
from keys import DG_TOKEN
from DataBase import DataBase

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
            database.cur.execute("insert into clients ")
            break
        break

if __name__ == "__main__":
    asyncio.run(colect_clients())