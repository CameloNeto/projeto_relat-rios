from pydantic import BaseModel

class ConfiguredBaseModel(BaseModel):
    """Base model configured for Pydantic v2 and compatibility with SQLAlchemy ORM objects.

    Uses `model_config['from_attributes'] = True` to allow parsing from ORM objects (SQLAlchemy instances).
    """

    model_config = {"from_attributes": True}
