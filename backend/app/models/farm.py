from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.core.database import Base


class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"), nullable=False)
    area_hectares = Column(Float)
    location_name = Column(String)
