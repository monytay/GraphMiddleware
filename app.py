import os
import requests
import json
import logging 
import azure.functions as func

access_token = None

def getAccessToken():
    global access_token
    if access_token:
      return access_token

    tenantID="test"
    clientID="test"
    clientSecret="test"
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
      
      if response.status_code == 200:
        tokenInfo = response.json()
        access_token = tokenInfo.get("access_token")
        return tokenInfo.get('access_token')
      else:
        print(errorMessage, response.text, "Response status code:", response.status_code)
    except Exception as e:
      print(errorMessage,e)
    return errorMessage









