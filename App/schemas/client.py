from typing import Optional
from pydantic import constr, ConfigDict
from .base import ConfiguredBaseModel
from .facility import FacilityBase
from typing import List


class ClientBase(ConfiguredBaseModel):
    name: constr(min_length=1)
    document_type: constr(min_length=1)
    document: constr(min_length=1)

    model_config = ConfigDict(from_attributes=True)

class ClientOut(ConfiguredBaseModel):
    name: constr(min_length=1)
    document_type: constr(min_length=1)
    document: constr(min_length=1)
    facilities: List[FacilityBase]

    model_config = ConfigDict(from_attributes=True)