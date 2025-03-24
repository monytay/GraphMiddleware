from app import getAccessToken
import requests

def getPrinters():
  try:
    
    token = getAccessToken()
    if not token:
      print("Failed to retrieve token")
      return None

    header = {
      "Authorization" : f'Bearer {token}',
      "Content-Type" : "application/json"
    }

    response = requests.get(f"https://graph.microsoft.com/beta/print/printers",headers=header)
    errorMessage="UniversalPrint API error"

    if response.status_code == 200:
      printersInfo = response.json()
      print(printersInfo)
      return printersInfo 
    else:
      print(errorMessage, response.text, "Response status code: ", response.status_code)
  except Exception as e:
    print(errorMessage,e)
  return None

if __name__ == "__main__":
    print("Starting app...")
    printers = getPrinters()
    print("Retrieved Printers Info:", printers)
