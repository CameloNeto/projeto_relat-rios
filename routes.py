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
from App.schemas.client import ClientOut


app = FastAPI()

@app.get("/clients/{document}", response_model=ClientOut)
def get_client(document:str) -> ClientOut:
    """Retorna um cliente pelo documento (usa `ClientRead` como schema de resposta)."""
    try:
        document = transform_document(document)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f'{error.args}')
    
    with db_session() as session:
        client_found = session.execute(select(client).where(client.document==document).options(selectinload(client.facilities))).scalar()
        if client_found is None:
            raise HTTPException(status_code=404, detail="Client not found")

        client_found = ClientOut.model_validate(client_found)

        return client_found

@app.get("/bills/{facility_number}")
def get_bills(facility_number:Union[str, int]):
    """"""
    from App.functions.data import clear_punctuation
    facility_number = clear_punctuation(facility_number)
    
    return ""


if __name__ == "__main__":
    print(get_client("358.219.143-53"))