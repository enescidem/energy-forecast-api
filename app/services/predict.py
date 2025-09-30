from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import pandas as pd
from app.models.energy import EnergyData

def predict_next_day(db: Session):
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    records = db.query(EnergyData).filter(EnergyData.date >= seven_days_ago).all()

    if not records:
        return None

    df = pd.DataFrame([{"date": r.date, "consumption": r.consumption} for r in records])
    avg_consumption = df["consumption"].mean()
    next_day = datetime.utcnow() + timedelta(days=1)

    return {
        "prediction_date": next_day.strftime("%Y-%m-%d"),
        "predicted_consumption": round(avg_consumption, 2),
        "records_used": len(df)
    }
