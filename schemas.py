from pydantic import BaseModel


class Address(BaseModel):

    type_col: str
    properties_id: str
    properties_unit: str
    properties_number: str
    properties_street: str
    properties_city: str
    properties_district: str
    properties_region: str
    properties_postcode: str
    properties_hash: str
    geometry_type: str
    geometry_coordinate_X: str
    geometry_coordinate_Y: str
    #pk_id: int

    class Config:
        orm_mode = True
