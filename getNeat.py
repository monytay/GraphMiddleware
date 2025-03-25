import requests

# Configure Bearer access token for authorization
access_token = 'put in your token'
orgid = 'put in your organization id'

# Set up the headers for the request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

# Construct the URL for the API request to list all rooms
url = f"https://api.pulse.neat.no/v1/orgs/{orgid}/rooms"
def getNeat():
    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        # Print the response data
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")  # Handle HTTP errors
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle other exceptions
