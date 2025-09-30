from fastapi import FastAPI
from app.routes import auth, data, predict
from app.database import Base, engine

app = FastAPI(title="Energy Forecast API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(data.router)
app.include_router(predict.router)