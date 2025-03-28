import getNeat
import app
import getPrinters
import getServices
import requests
from fastapi import FastAPI

token = app.getAccessToken()

app = FastAPI()

@app.get("/api/printers")
async def get_printers():
    printerData = getPrinters.getPrinters()
    return {
        "token: " : token,
        "Printers" : printerData
    }

@app.get("/api/neat")
async def get_neat():
    neatData = getNeat.getNeat()
    return {
        "token" : token,
        "Meeting Room's" : neatData
    }

@app.get("/api/services")
async def get_services():
    servicesData = getServices.getServices()
    return {
        "token" : token,
        "Microsoft Services" : servicesData
    }
