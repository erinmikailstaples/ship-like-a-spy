from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}


# # from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Annotated
# import os
# import uvicorn
# import pymysql
# ## from the launchdarkly sdk
# from ldclient.config import Config

# ## make sure LD is installed in your environment
# ### use pip install launchdarkly-server-sdk

# LD_KEY = os.environ.get('LD_SERVER_KEY')

# ## configure your LD SDK Key
# ldclient.set_config(Config(sdk_key="YOUR_SDK_KEY"))

# ##  set your LD context
# ## context = 
# ## Context.builder("context-key-123abc").name(Erin).build()

# ## Evaluate your flag
# ## val = client.variation('qrcode', context, False)
