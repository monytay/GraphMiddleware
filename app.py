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
        "tenant_id" : "test",
        "client_id" : "test2",
        "client_secret" : "secret",
      }
      response = requests.post(f'http://localhost:8002/getToken/', json = data)
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

if __name__ == "__main__":
    print("Starting app...")
    token = getAccessToken()
    print("Retrieved Token:", token)


