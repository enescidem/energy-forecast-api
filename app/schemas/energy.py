from pydantic import BaseModel
import datetime

class EnergyDataBase(BaseModel):
    date: datetime.datetime
    consumption: float

class EnergyDataCreate(EnergyDataBase):
    pass

class EnergyDataResponse(EnergyDataBase):
    id: int
    class Config:
        from_attributes = True
