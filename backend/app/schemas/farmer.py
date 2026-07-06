from pydantic import BaseModel


class FarmerBase(BaseModel):
    name: str
    phone: str


class FarmerCreate(FarmerBase):
    pass


class FarmerOut(FarmerBase):
    id: int

    class Config:
        from_attributes = True
