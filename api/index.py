from fastapi import FastAPI
# import launchdarkly_server_sdk as ldclient
import ldclient
from ldclient.config import Config

# create the FastAPI app

app = FastAPI()

# sample user for LD purposes - static user here for testing
user =  {
    "key": "007",
    "firstName": "James",
    "lastName": "Bond",
    "email": "spystuff007@example.com",
    "custom": {
        "groups": ["superspy"]
    }
}

@app.get("/api/python")
def hello_world():
    print("the name's bond, james bond🍸")
# # here is where we'll launch some LD magic with our feature flags
# # your keys can be foudn on the Account settings page under the Environments tab for each project.
#     ldclient.set_config(Config("sdk-5709bc2e-ae00-450a-b3d8-3adf981ffd5"))
#     show_feature = ldclient.variation("earlyLaunch", user, False)
#     if show_feature:
#         print("earlyLaunch is ON!!!")
#     else:
#         print("earlyLaunch is OFF!!!")

# ldclient.close()



# ldclient = LDClient("0")




