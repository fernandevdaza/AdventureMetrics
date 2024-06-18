from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

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

class CountryRegion(Base):
    __tablename__ = 'countryregion'
    __table_args__ = {'schema': 'person'}
    countryregioncode = Column(String, primary_key=True)
    name = Column(String)
    modifieddate = Column(DateTime)
    provincias = relationship("StateProvince", back_populates="pais")

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

class StateProvince(Base):
    __tablename__ = 'stateprovince'
    __table_args__ = {'schema': 'person'}
    stateprovinceid = Column(Integer, primary_key=True)
    stateprovincecode = Column(String)
    countryregioncode = Column(String, ForeignKey('person.countryregion.countryregioncode'))
    isonlystateprovinceflag = Column(Integer)
    name = Column(String)
    territoryid = Column(Integer, ForeignKey('sales.salesterritory.territoryid'))
    rowguid = Column(String)
    modifieddate = Column(DateTime)
    ciudades = relationship("Address", back_populates="provincia")
    territorio = relationship("SalesTerritory", back_populates="provincia")
    pais = relationship("CountryRegion", back_populates="provincias")
