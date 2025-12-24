from pydantic import BaseModel, ConfigDict

from App.models.base import Base
from App.models.client import client
from App.models.email import email
from App.models.facility import facility
from App.models.bill import bill

class Client_checker(BaseModel):
    id: int
    name: str
    document_type: Mapped[str] = mapped_column(String, nullable=False)
    document: Mapped[str] = mapped_column(String, nullable=False)