# aggregator/app.py
import os
import asyncio
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI(title="Aggregator JSON Service")

rf_original = os.getenv("rf_original", "http://localhost:8001/data")
rf_cross_val = os.getenv("rf_cross_val", "http://localhost:8002/data")


@app.get("/", response_class=JSONResponse)
async def aggregated_data():
    async with httpx.AsyncClient(timeout=10.0) as client:
        resp_a, resp_b = await asyncio.gather(
            client.get(rf_original),
            client.get(rf_cross_val),
        )

    data_a = resp_a.json() if resp_a.status_code == 200 else {"error": "rf_original unavailable"}
    data_b = resp_b.json() if resp_b.status_code == 200 else {"error": "rf_cross_val unavailable"}

    return {
        "rf_original": data_a,
        "rf_cross_val": data_b,
    }


@app.get("/health")
def health():
    return {
        "status": "aggregator running",
        "service_a_url": rf_original,
        "service_b_url": rf_cross_val,
    }
