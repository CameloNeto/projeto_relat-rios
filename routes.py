from fastapi import FastAPI, HTTPException
from App.models.make_session import db_session
from typing import Union
from App.functions.documents import transform_document
from sqlalchemy import select
from App.models.client import client
from App.models.email import email
from App.models.facility import facility
from App.models.bill import bill


app = FastAPI()

@app.get("/clients/{document}")
def get_client(document:Union[str, int]):
    """"""
    try:
        document = transform_document(document)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f'{error.args}')
    
    with db_session() as session:
        client_found = session.execute(select(client).where(client.document==document)).scalar_one_or_none()
        

        emails = session.execute(select(email).where(email.client_id==client_found.id)).all()
        emails = [e[0].email for e in emails]
        
        facilities = session.execute(select(facility).where(facility.client_id==client_found.id)).all()
        facilities = [f[0].number for f in facilities]

@app.get("/bills/{facility_number}")
def get_bills(facility_number:Union[str, int]):
    """"""
    return ""