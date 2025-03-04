import os
import requests
import json
import logging 
import azure.functions as func

tenantID="test"
clientID="test2"
clientSecret="secret"
scope = "https://www.graph.microsoft.com/.default" 


def getAccessToken():
    try:
      data = {
        "grant_type" : "client_credentials",
        "client_id" : clientID,
        "tenant_id" : tenantID,
        "clientSecret" : clientSecret,
        "scope" : scope
      }
      response = requests.post(f'http://localhost:8002/getToken/', data=data)
      errorMessage="Token retrieval error"

      if response.status_code == 200:
        tokenInfo = response.json()
        print("AccessToken:",tokenInfo.get('AccessToken'))
        return tokenInfo.get('AccessToken')
    except:
      print(errorMessage)
      return errorMessage

def getPrinters():
  try:
    
    token = getAccessToken()
    header = {
      "Authorization" : f'Bearer{token}',
      "Content-Type" : "application/json"
    }
    response = requests.get(f"https://graph.microsoft.com/PrinterShare.Read.All",headers=header)
    errorMessage="UniversalPrint API error"

    if response.status() == 200:
      printersInfo = response.json(),
      return printersInfo 
  except:
    return errorMessage
