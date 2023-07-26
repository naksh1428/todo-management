from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dbconnection import Base


class Address(Base):
    __tablename__ = "address"

    type_col = Column(String)
    properties_id = Column(String)
    properties_unit = Column(String)
    properties_number = Column(String)
    properties_street = Column(String)
    properties_city = Column(String)
    properties_district = Column(String)
    properties_region = Column(String)
    properties_postcode = Column(String)
    properties_hash = Column(String)
    geometry_type = Column(String)
    geometry_coordinate_X = Column(String)
    geometry_coordinate_Y = Column(String)
    pk_id = Column(Integer, primary_key=True, index=True)
