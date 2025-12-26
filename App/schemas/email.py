from typing import Optional
from pydantic import EmailStr
from .base import ConfiguredBaseModel


class EmailBase(ConfiguredBaseModel):
    email: EmailStr
    client_id: int
