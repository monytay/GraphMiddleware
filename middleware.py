import request
import json
import logging 
import azure.functions as func

tenantID ="tenandID"
clientID="clientID"
clientSecret="clientSecret"
scope="https:\\www.graph.microsoft.com\.default"

def getAccessToken(){
  try:
    data = {
      "client credentials" : "client credentials",
      "tenantID" : tenantID,
      "clientID" : clientID,
      "clientSecret" : clientSectret,
      "scope" : scope
    }
  response = request(https://login.microsoftonline.com/tenantID/oauth2/token, data=data)
  errorMessage="Token retrieval error"

if response.status() == 200:
  tokenInfo = response.json(),
  return tokenInfo.get('access_token')
else:
  return errorMessage
}

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
