from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = {'schema': 'person'}
    businessentityid = Column(Integer, primary_key=True)
    person_type = Column(String)
    namestyle = Column(Integer)
    title = Column(String, nullable=True)
    firstname = Column(String)
    middlename = Column(String, nullable=True)
    lastname = Column(String)
    suffix = Column(String, nullable=True)
    email = Column(String, nullable=True)
    emailpromotion = Column(Integer)
    additionalcontactinfo = Column(String, nullable=True)
    demographics = Column(String, nullable=True)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    direccion = relationship("Address", back_populates="personas")
    cliente = relationship("Customer", back_populates="persona")