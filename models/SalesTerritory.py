from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class SalesTerritory(Base):
    __tablename__ = 'salesterritory'
    __table_args__ = {'schema': 'sales'}
    territoryid = Column(Integer, primary_key=True)
    name = Column(String)
    countryregioncode = Column(String)
    group = Column(String)
    salesytd = Column(Float)
    saleslastyear = Column(Float)
    costytd = Column(Float)
    costlastyear = Column(Float)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    clientes = relationship("Customer", back_populates="territorio")
    provincia = relationship("StateProvince", back_populates="territorio")