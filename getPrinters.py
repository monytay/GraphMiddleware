from app import getAccessToken
import requests

def getPrinters():
  try:
    
    token = getAccessToken()
    header = {
      "Authorization" : f'Bearer {token}',
      "Content-Type" : "application/json"
    }
    response = requests.get(f"https://graph.microsoft.com/PrinterShare.Read.All",headers=header)
    errorMessage="UniversalPrint API error"

    if response.status_code == 200:
      printersInfo = response.json()
      return printersInfo 
  except Exception as e:
    print(errorMessage,e)
  return errorMessage
