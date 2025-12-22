import httpx
import asyncio
from keys import DG_TOKEN
import json
from sqlalchemy import insert, select, exists, inspect
from App.models import client
from App.models.make_session import db_session
from App.models.email import email
from uuid import uuid4


async def colect_emails():
    urlDG = 'https://gestao.dg.energy/api/v1/entities/'

    headersDG = {
            'Authorization':f'Token {DG_TOKEN}'
        }

    with db_session() as session:
        while urlDG:
            request = await httpx.AsyncClient(timeout=120).request("GET", urlDG, headers=headersDG)
            results = request.json().get("results")
            for dg_client in results:

                dg_emails = dg_client.get("emails")
                if type(dg_emails) is not list:
                    dg_emails = json.loads(dg_emails)

                db_emails_obj = session.execute(select(email).where(email.client_id==dg_client.get("id"))).all()
                db_emails = [db_email[0].email for db_email in db_emails_obj]

                if db_emails == dg_emails:
                    continue

                for db_email_obj in db_emails_obj:
                    if db_email_obj[0].email in dg_emails:
                        continue
                    else:
                        session.delete(db_email_obj[0])
                        session.commit()
            
                for dg_email in dg_emails:
                    if dg_email in db_emails:
                        continue
                    else:
                        add_email = insert(email).values(email=dg_email, client_id=dg_client.get("id"))
                        session.execute(add_email)
                        session.commit()

            urlDG = request.json().get("next")

if __name__ == "__main__":
    asyncio.run(colect_emails())