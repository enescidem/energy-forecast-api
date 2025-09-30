from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction_date: str
    predicted_consumption: float
    records_used: int

    class Config:
        from_attributes = True
