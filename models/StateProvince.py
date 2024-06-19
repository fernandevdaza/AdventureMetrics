from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base

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
