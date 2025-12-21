import httpx
import asyncio
from keys import DG_TOKEN
import json
from sqlalchemy import insert, select, exists
from models import client
from models.make_session import db_session
from models.email import email
from uuid import uuid4


async def get_facilities(document:str) -> List[str]:
        """
        Docstring for get_facilities

        :return: Retorna uma lista de strings com os números das instalações
        :rtype: List[tuple]
        """
        
        urlDG = 'https://gestao.dg.energy/api/v1/installations/'

        headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

        facilities = []

        while urlDG:
            request = await httpx.AsyncClient(timeout=240).request("GET", urlDG, headers=headersDG)
            results = request.json().get("results")
            for facility in results:
                if facility.get('owner') == document:
                    facilities.append(facility.get('number'))
            urlDG = request.json().get("next")
        return facilities

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

                email_list = dg_client.get("emails")
                if type(email_list) is not list:
                    email_list = json.loads(email_list)

                for dg_email in email_list:
                    if not session.scalar(select(exists().where(email.email == dg_email, email.client_id == dg_client.get("id")))):
                        add_email = insert(email).values(
                            #id= str(uuid4()),
                            email = dg_email,
                            client_id = dg_client.get("id")
                        )
                        session.execute(add_email)
                        session.commit()

            urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_clients())