from typing import Optional
from pydantic import conint
from .base import ConfiguredBaseModel


class FacilityBase(ConfiguredBaseModel):
    number: conint(strict=True)
    client_id: int


