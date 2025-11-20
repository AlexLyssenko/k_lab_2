from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

app = FastAPI(title="rf_cross_val_predictor")


model = joblib.load("iris_model_org.pkl")


class PredictRequest(BaseModel):
    features: List[float]


class PredictResponse(BaseModel):
    prediction: int


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    arr = np.array(req.features).reshape(1, -1)
    pred = int(model.predict(arr)[0])
    return PredictResponse(prediction=pred)


@app.get("/")
def root():
    return {"status": "model service running"}
