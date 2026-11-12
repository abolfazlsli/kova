from sqlalchemy import *
from sqlalchemy.orm import *
import uuid


engine = create_engine(
    "sqlite:///database.db"
)


def create_random_id () :
    return str(uuid.uuid4())

class Base(DeclarativeBase) :
    pass

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
       db.close()
class BasicTabale (Base) :
    __abstract__ = True
    id = Column(Integer , primary_key=True)
    public_id = Column(String , nullable=False , unique=True , default=create_random_id)
