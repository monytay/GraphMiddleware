import os
import requests
import json
import logging 
import azure.functions as func
import getNeat
import getPrinters
import getServices
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def allData():
    data = {
    printers = getPrinters(),
    services = getServices(),
    neat = getNeat()
    }

    return data
    
def getAccessToken():
    tenantID="Real id from azzure"
    clientID="real client id from azure"
    clientSecret="real client secret from azure"
    scope = "https://www.graph.microsoft.com/.default" 

    url = f"https://login.microsoftonline.com/{tenantID}/oauth2/v2.0/token"

    data = {
        "grant_type" : "client_credentials",
        "client_id" : clientID,
        "client_secret" : clientSecret,
        "scope": "https://graph.microsoft.com/.default"
      }

    try:
      response = requests.post(url, data = data)
      errorMessage="Token retrieval error"

      print("Sending request to get access token...")  # Debugging line
      print("Request payload:", data)  # Print the data being sent

      if response.status_code == 200:
        tokenInfo = response.json()
        print("AccessToken:",tokenInfo.get('access_token'))
        return tokenInfo.get('access_token')
      else:
        print(errorMessage, response.text, "Response status code:", response.status_code)
    except Exception as e:
      print(errorMessage,e)
    return errorMessage

if __name__ == __main__:
    import uvicorn
    uvicorn.run(app, host=0.0.0.0, port=8000)




