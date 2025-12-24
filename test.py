from fastapi import FastAPI, HTTPException
from App.models.make_session import db_session
from typing import Union
from App.functions.documents import transform_document
from sqlalchemy import select
from App.models.client import client
from App.models.email import email
from App.models.facility import facility
from App.models.bill import bill
import json

document = "358.219.143-53"

with db_session() as session:
        client_found = session.execute(select(client).where(client.document==document)).scalar_one_or_none()
        emails = session.execute(select(email).where(email.client_id==client_found.id)).all()
        emails = [e[0].email for e in emails]
        facilities = session.execute(select(facility).where(facility.client_id==client_found.id)).all()
        facilities = [f[0].number for f in facilities]
        print(facilities)