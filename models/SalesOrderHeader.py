from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base


class SalesOrderHeader(Base):
    __tablename__ = 'salesorderheader'
    __table_args__ = {'schema': 'sales'}
    salesorderid = Column(Integer, primary_key=True)
    revisionnumber = Column(Integer)
    orderdate = Column(DateTime)
    duedate = Column(DateTime)
    shipdate = Column(DateTime, nullable=True)
    status = Column(Integer)
    onlineorderflag = Column(Integer)
    purchaseordernumber = Column(String, nullable=True)
    accountnumber = Column(String, nullable=True)
    customerid = Column(Integer, ForeignKey('sales.customer.customerid'))
    salespersonid = Column(Integer, nullable=True)
    territoryid = Column(Integer, nullable=True)
    billtoaddressid = Column(Integer)
    shiptoaddressid = Column(Integer)
    shipmethodid = Column(Integer)
    creditcardid = Column(Integer, nullable=True)
    creditcardapprovalcode = Column(String, nullable=True)
    currencyrateid = Column(Integer, nullable=True)
    subtotal = Column(Float)
    taxamt = Column(Float)
    freight = Column(Float)
    totaldue = Column(Float)
    comment = Column(String, nullable=True)
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    customer = relationship("Customer", back_populates="ventas")
    detalle_ventas = relationship("SalesOrderDetail", back_populates="venta")