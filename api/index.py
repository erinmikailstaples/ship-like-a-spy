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

# Retrieve MySQL credentials from environment variables
mysql_user = os.getenv("MYSQLUSER")
mysql_password = os.getenv("MYSQLPASSWORD")
mysql_host = os.getenv("MYSQLHOST")
mysql_database = os.getenv("MYSQLDATABASE")
mysql_port = os.getenv("MYSQLPORT")

# Create a MySQL connection
mysql_connection = pymysql.connect(
    user=mysql_user,
    password=mysql_password,
    host=mysql_host,
    database=mysql_database,
    port=int(mysql_port)  # Ensure the port is an integer
)

app = FastAPI()

@app.get("/")
async def list_data():
    cursor = mysql_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM bonddata")  # Replace 'bonddata' with your table name
    data = cursor.fetchall()
    cursor.close()

    return {"data": data}

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("MYSQLHOST"), port=36985)


