from dotenv import load_dotenv
import os
import requests
import json
import logging 
import azure.functions as func

load_dotenv()

tenantID = os.getenv("tenantID")
clientID = os.getenv('clientID')
client_secret = os.getenv("clientSecret")
scope = os.getenv("scope")

def getAccessToken():
    try:
      data = {
        "grant_type" : "client_credentials",
        "clientID" : clientID,
        "tenantID" : tenantID,
        "scope" : scope
      }
      response = requests.post(f'https://login.microsoftonline.com/{tenantID}/oauth2/token', data=data)
      errorMessage="Token retrieval error"

      if response.status_code() == 200:
        tokenInfo = response.json(),
        return tokenInfo.get('access_token')
    except:
      return errorMessage

def getPrinters():
  try:
    
    token = getAccessToken()
    header = {
      "Authorization" : f'Bearer{token}',
      "Content-Type" : "application/json"
    }
    response = request(f"https://graph.microsoft.com/PrinterShare.Read.All",headers=headers)
    errorMessage="UniversalPrint API error"

    if response.status() == 200:
      printersInfo = response.json(),
      return printersInfo 
  except:
    return errorMessage
