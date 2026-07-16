from fastapi import FastAPI
from database import engine, Base
from models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"status": "ok"}