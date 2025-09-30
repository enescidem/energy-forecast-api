from sqlalchemy.orm import Session
from .. import models, schemas

def create_energy_data(db: Session, data: schemas.EnergyDataCreate):
    db_data = models.EnergyData(
        date=data.date,
        consumption=data.consumption
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_energy_data(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.EnergyData).offset(skip).limit(limit).all()
