from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base

class SalesOrderDetail(Base):
    __tablename__ = 'salesorderdetail'
    __table_args__ = {'schema': 'sales'}
    salesorderid = Column(Integer, ForeignKey('sales.salesorderheader.salesorderid'), primary_key=True)
    salesorderdetailid = Column(Integer, primary_key=True)
    carriertrackingnumber = Column(String, nullable=True)
    orderqty = Column(Integer)
    productid = Column(Integer, ForeignKey('production.product.productid'))
    specialofferid = Column(Integer)
    unitprice = Column(Float)
    unitpricediscount = Column(Float)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    producto = relationship("Product", back_populates="detalles_ventas")
    venta = relationship("SalesOrderHeader", back_populates="detalle_ventas")