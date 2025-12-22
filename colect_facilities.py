import httpx
import asyncio
from keys import DG_TOKEN
import json
from sqlalchemy import insert, select, exists
from models.make_session import db_session
from models.facility import facility
from models.client import client


async def colect_facilities():
    urlDG = 'https://gestao.dg.energy/api/v1/installations/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    with db_session() as session:
        while urlDG:
            request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
            #print(request)
            results = request.json().get("results")
            #print(results)
            for dg_facility in results:
                #print(dg_facility)
                condition = session.scalar(select(exists().where(facility.number==dg_facility.get("number"))))
                session.query(client).where(client.document==dg_facility.get("owner")).first()
                if not condition:
                    client_found = session.query(client).where(client.document==dg_facility.get("owner")).first()
                    
                    add_facility = insert(facility).values(
                    number=dg_facility.get("number"),
                    client_id=client_found.id)
                    session.execute(add_facility)
                    session.commit()

            urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_facilities())