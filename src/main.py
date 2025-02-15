from fastapi import FastAPI, HTTPException
from pathlib import Path
import os

app = FastAPI()

@app.post("/run")
async def run_task(task: str):
    return {"status": "Task received"}

@app.get("/read")
async def read_file(path: str):
    if not path.startswith('/data'):
        raise HTTPException(status_code=403)
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404)
