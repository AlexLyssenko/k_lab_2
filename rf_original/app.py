# service_a/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="rf_original")

class Item(BaseModel):
    id: int
    name: str
    value: float

@app.get("/data", response_model=List[Item])
def get_data():
    # sample static data; could be from DB in real app
    return [
        {"id": 1, "name": "A-one", "value": 12.34},
        {"id": 2, "name": "A-two", "value": 56.78}
    ]

@app.get("/")
def root():
    return {"status": "rf_original running"}
