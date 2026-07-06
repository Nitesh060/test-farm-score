from sqlalchemy import Column, DateTime, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.base import Base


class Farm(Base):
    __tablename__ = "farms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    farmer_id = Column(
        UUID(as_uuid=True),
        ForeignKey("farmers.id"),
        nullable=False,
    )

    survey_number = Column(String(100))

    village = Column(String(150))

    taluka = Column(String(150))

    district = Column(String(150))

    state = Column(String(150))

    country = Column(String(100), default="India")

    pincode = Column(String(10))

    land_use_type = Column(String(100))

    irrigation_type = Column(String(100))

    centroid_lat = Column(Numeric(10, 7))

    centroid_lon = Column(Numeric(10, 7))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
