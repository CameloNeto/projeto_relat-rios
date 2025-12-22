from sqlalchemy.orm import sessionmaker
from .engine import engine

db_session = sessionmaker(engine)