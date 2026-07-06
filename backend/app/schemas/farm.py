from pydantic import BaseModel


class FarmBase(BaseModel):
    farmer_id: int
    area_hectares: float
    location_name: str


class FarmCreate(FarmBase):
    pass


class FarmOut(FarmBase):
    id: int

    class Config:
        from_attributes = True
