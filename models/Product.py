from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from db.connection import Base

class Product(Base):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'production'}
    productid = Column(Integer, primary_key=True)
    name = Column(String)
    productnumber = Column(String)
    color = Column(String, nullable=True)
    standardcost = Column(Float)
    listprice = Column(Float)
    size = Column(String, nullable=True)
    weight = Column(Float, nullable=True)
    sellstartdate = Column(DateTime)
    sellenddate = Column(DateTime, nullable=True)
    discontinueddate = Column(DateTime, nullable=True)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    detalles_ventas = relationship("SalesOrderDetail", back_populates="producto")