from sqlalchemy.orm import sessionmaker
from models.engine import engine

db_session = sessionmaker(engine)