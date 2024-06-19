from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class Customer(Base):
    __tablename__ = 'customer'
    __table_args__ = {'schema': 'sales'}
    customerid = Column(Integer, primary_key=True)
    personid = Column(Integer, ForeignKey('person.person.businessentityid'), nullable=True)
    storeid = Column(Integer, nullable=True)
    territoryid = Column(Integer, ForeignKey('sales.salesterritory.territoryid'), nullable=True)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    ventas = relationship("SalesOrderHeader", back_populates="customer")
    persona = relationship("Person", back_populates="cliente")
    territorio = relationship("SalesTerritory", back_populates="clientes")