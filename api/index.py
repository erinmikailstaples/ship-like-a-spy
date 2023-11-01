from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
import os
import uvicorn
import pymysql

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}
