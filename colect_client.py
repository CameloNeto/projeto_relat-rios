import httpx
import asyncio
from keys import DG_TOKEN
import json
from sqlalchemy import insert, select
from models.make_session import db_session
from models.client import client


async def colect_clients():
    urlDG = 'https://gestao.dg.energy/api/v1/entities/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    with db_session() as session:
        while urlDG:
            request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
            results = request.json().get("results")
            for dg_client in results:
                
                client_count = session.query(client).where(client.id == dg_client.get('id')).count()
                if client_count == 0:
                    add_client = insert(client).values(
                    id=dg_client.get("id"),
                    name=dg_client.get("name"),
                    document_type=dg_client.get("document_type"),
                    document=dg_client.get("document")
                    )
                    session.execute(add_client)
                    session.commit()

            urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_clients())