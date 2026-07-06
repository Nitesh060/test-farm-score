from sqlalchemy.orm import Session
from app.models.farmer import Farmer


class FarmerRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, farmer_id: int):
        return self.db.query(Farmer).filter(Farmer.id == farmer_id).first()

    def list(self):
        return self.db.query(Farmer).all()

    def create(self, farmer: Farmer):
        self.db.add(farmer)
        self.db.commit()
        self.db.refresh(farmer)
        return farmer
