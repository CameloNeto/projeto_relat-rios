from typing import Optional
from pydantic import constr
from .base import ConfiguredBaseModel


class ClientBase(ConfiguredBaseModel):
    name: constr(min_length=1)
    document_type: constr(min_length=1)
    document: constr(min_length=1)