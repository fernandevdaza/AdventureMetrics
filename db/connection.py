from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")

DATABASE_URI = config.get("DATABASE_URI")

def get_engine():
    return create_engine(DATABASE_URI)


Base = declarative_base()

# Crea el motor de conexión

SessionLocal = sessionmaker(autoflush=False, bind=get_engine())


