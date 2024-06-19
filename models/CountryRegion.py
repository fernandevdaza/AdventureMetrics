from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base

class CountryRegion(Base):
    __tablename__ = 'countryregion'
    __table_args__ = {'schema': 'person'}
    countryregioncode = Column(String, primary_key=True)
    name = Column(String)
    modifieddate = Column(DateTime)
    provincias = relationship("StateProvince", back_populates="pais")