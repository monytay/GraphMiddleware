from app import getAccessToken
import requests

def getServices():
    try:

      token = getAccessToken()
      if not token:
          print("Error retrieving the token ")
          return None
      
      header = {
        "Authorization" : f'Bearer {token}',
        "Content-Type" : "application/json"
      }

      response = requests.get("https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews", headers=header)
      errorMessage = "Microsoft Graph API Service health check error"

      if response.status_code == 200:
          servicesInfo = response.json()
          print(servicesInfo)
          return servicesInfo
      else:
          print(errorMessage, "Error status code:",response.status_code)
          return(response.status_code)
    except Exception as e:
        print(errorMessage, e)
    return None
        
if __name__ == "__main__":
    print("Starting app...")
    services = getServices()
    print("Retrieved Printers Info:", services)
