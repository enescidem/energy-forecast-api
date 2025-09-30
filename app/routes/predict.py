from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.predict import PredictionResponse
from app.services.predict import predict_next_day as predict_service

router = APIRouter(prefix="/predict", tags=["predict"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=PredictionResponse)
def predict_next_day(db: Session = Depends(get_db)):
    result = predict_service(db)
    if not result:
        raise HTTPException(status_code=404, detail="No data available for prediction")
    return result
