import sqlite3
import httpx
import asyncio
from keys import DG_TOKEN

def connect_db():
con = sqlite3.connect('./database/database.db')
cur = con.cursor()

async def colect_clients():
    urlDG = 'https://gestao.dg.energy/api/v1/entities/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    while urlDG:
        request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
        results = request.json().get("results")
        for client in results:
            
            break
        break

if __name__ == "__main__":
    asyncio.run(colect_clients())