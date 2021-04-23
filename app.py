from fastapi import FastAPI
import uvicorn
import json


# Init
app = FastAPI(debug=True)

# Data

with open("covid_india.json") as f:
    india = json.load(f)

@app.get('/india')
async def get_india():
    return {"india": india}

with open("covid_brazil.json") as f:
    brazil = json.load(f)

@app.get('/brazil')
async def get_brazil():
    return {"brazil": brazil}

# if __name__ == '__main__':
#     uvicorn.run(app,host="127.0.0.1",port="8000")