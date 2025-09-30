from sqlalchemy import Column, Integer, Float, DateTime
from ..database import Base
import datetime

class EnergyData(Base):
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    consumption = Column(Float)
