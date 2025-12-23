from fastapi import FastAPI, HTTPException
from App.models.make_session import db_session
from typing import Union

app = FastAPI()

@app.get("/clients/{document}")
def get_client(document:Union[str, int]):
    """"""
    if type(str):
        document_size = len(document)
        if document_size not in [11, 14, 18]:
            """"""
        else:
            raise HTTPException(status_code=400, detail="Invalid document format")
    else:


@app.get("/bills/{facility_number}")
def get_bills(facility_number:Union[str, int]):
    """"""
    return ""