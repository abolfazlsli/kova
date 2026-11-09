from sqlalchemy import *
from sqlalchemy.orm import *
import uuid


engine = create_engine(
    "sqlite:///database.db"
)


def create_random_id () :
    return uuid.uuid8()

class Base(DeclarativeBase) :
    pass


def get_db () :
    db = sessionmaker()
    return db

class BasicTabale (Base) :
    __abstract__ = True
    id = Column(Integer , primary_key=True)
    public_id = Column(String , nullable=False , unique=True , default=create_random_id)
