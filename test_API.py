from fastapi import FastAPI, HTTPException
from App.models.make_session import db_session
from typing import Union
from App.functions.documents import transform_document
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from App.models.client import client
from App.models.email import email
from App.models.facility import facility
from App.models.bill import bill
import json
import httpx
import asyncio

document = "358.219.143-53"

async def test_client_path():
        test_base_url = "http://127.0.0.1:8000/clients/"
        with db_session() as session:
                clients = session.execute(select(client).where().limit(100).order_by(client.id).options(selectinload(client.facilities))).all()
                for test_data in clients:
                        async with httpx.AsyncClient() as request_client:
                                data = await request_client.get(f"{test_base_url}{test_data[0].document}")
                                print(data)
                                print(data, data.json())

if __name__ == "__main__":
        asyncio.run(test_client_path())