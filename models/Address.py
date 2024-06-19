from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class Address(Base):
    __tablename__ = 'address'
    __table_args__ = {'schema': 'person'}
    addressid = Column(Integer, primary_key=True)
    addressline1 = Column(String)
    addressline2 = Column(String, nullable=True)
    city = Column(String)
    stateprovinceid = Column(Integer, ForeignKey('person.stateprovince.stateprovinceid'))
    postalcode = Column(String)
    spatiallocation = Column(String, nullable=True)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    personid = Column(Integer, ForeignKey('person.person.businessentityid'))
    personas = relationship("Person", back_populates="direccion")
    provincia = relationship("StateProvince", back_populates="ciudades")
