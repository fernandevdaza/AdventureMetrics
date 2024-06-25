from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values
from contextlib import contextmanager


config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI")

def get_engine():
    return create_engine(
    DATABASE_URI,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800
)

engine = get_engine()
Session = sessionmaker(autoflush=False, bind=engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()




