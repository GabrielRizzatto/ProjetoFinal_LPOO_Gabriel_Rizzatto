from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URl")

engine = create_engine(DB_URL)

def pegar_session():
    try:
        Session = sessionmaker(bind = engine)
        session = Session()
        yield session
    finally:
        session.close()
