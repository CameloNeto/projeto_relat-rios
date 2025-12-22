from uuid import uuid4
from keys import DG_TOKEN
from App.models.base import Base
from App.models.engine import engine
from pathlib import Path
from os import mkdir

if not Path("./database/").exists():
    mkdir("./database")

Base.metadata.create_all(engine)

