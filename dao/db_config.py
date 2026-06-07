from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine, expire_on_commit=False)

@contextmanager
def pegar_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()