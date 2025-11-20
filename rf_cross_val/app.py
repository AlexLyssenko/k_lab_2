# service_b/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="rf_cross_val")

class Record(BaseModel):
    key: str
    description: str

@app.get("/data", response_model=List[Record])
def get_data():
    return [
        {"key": "B-1", "description": "Description one"},
        {"key": "B-2", "description": "Description two"}
    ]

@app.get("/")
def root():
    return {"status": "rf_cross_val running"}
