from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated
import os
import uvicorn
import pymysql

## make sure LD is installed in your environment
### pip install launchdarkly-server-sdk
## from ldclient.config import Config

## configure your LD SDK Key
### ldclient.set_config(Config(sdk_key="YOUR_SDK_KEY"))

##  set your LD context
## context = 
## Context.builder("context-key-123abc").name(Erin).build()

## Evaluate your flag
## val = client.variation('qrcode', context, False)

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


