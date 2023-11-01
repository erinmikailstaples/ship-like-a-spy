from fastapi import FastAPI
# import launchdarkly_server_sdk as ldclient
import ldclient
from ldclient.config import Config
import os

from fastapi import FastAPI

# create the FastAPI app

app = FastAPI()

# sample user for LD purposes - static user here for testing
# user =  {
#     "key": "user-key-123abc",
#     "firstName": "James",
#     "lastName": "Bond",
#     "email": "spystuff007@example.com",
#     "custom": {
#         "groups": ["superspy"]
#     }
# }


@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}
# here is where we'll launch some LD magic with our feature flags
# your keys can be foudn on the Account settings page under the Environments tab for each project.
    ldclient.set_config(Config(sdk_key="YOUR_SDK_KEY"))
    show_feature = ldclient.variation("earlyLaunch", user, False)
    if show_feature == True:
        return {"message": "Beta Feature is ON"}


LD_KEY = os.environ.get('LD_SERVER_KEY')





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
