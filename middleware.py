from dotenv import load_dotenv
import os
import requests
import json
import logging 
import azure.functions as func

load_dotenv():

tenantID = os.get("tenantID")
clientID = os.get('clientID')
client_secret = os.get("clientSecret")
scope = os.get("scope")

def getAccessToken():
    try:
        data = {
      "grant_type" : "client_credentials",
      "tenantID" : tenantID,
      "clientID" : clientID,
      "clientSecret" : clientSectret,
      "scope" : scope
    }
    response = requests.post(https://login.microsoftonline.com/{tenantID}/oauth2/token, data=data)
    errorMessage="Token retrieval error"

    if response.status_code() == 200:
    tokenInfo = response.json(),
    return tokenInfo.get('access_token')
    else:
    return errorMessage


def getPrinters(){
  try:
    headers = {
      token = getAccessToken()
      "Authorization" : f`Bearer{token}`,
      "Content-Type" : "application/json"
    }
    response = request(https://graph.microsoft.com/PrinterShare.Read.All,headers=headers)
    errorMessage="UniversalPrint API error"

  if response.status() == 200:
    printersInfo = response.json(),
    return printersInfo 
  else:
    return errorMessage
}
