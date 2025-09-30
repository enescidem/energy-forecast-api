from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import pandas as pd
from .. import schemas
from ..services import energy as energy_service
from ..database import get_db

router = APIRouter(prefix="/data", tags=["data"])

@router.post("/", response_model=schemas.EnergyDataResponse)
def create_data(data: schemas.EnergyDataCreate, db: Session = Depends(get_db)):
    return energy_service.create_energy_data(db=db, data=data)

@router.get("/", response_model=list[schemas.EnergyDataResponse])
def read_data(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return energy_service.get_energy_data(db=db, skip=skip, limit=limit)

@router.post("/upload-csv/")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Sadece CSV dosyası yükleyebilirsiniz")
    
    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Dosya okunamadı: {e}")

    required_columns = {"date", "consumption"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"CSV sütunları eksik. Gerekenler: {required_columns}")

    added_rows = []
    for _, row in df.iterrows():
        data = schemas.EnergyDataCreate(
            date=pd.to_datetime(row["date"]),
            consumption=float(row["consumption"])
        )
        db_row = energy_service.create_energy_data(db, data)
        added_rows.append(db_row)

    return {"message": f"{len(added_rows)} kayıt eklendi."}
