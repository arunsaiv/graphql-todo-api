# db.py
from sqlmodel import SQLModel, Session, create_engine
from model import Todo

sqlite_url = "sqlite:///./todos.db"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)