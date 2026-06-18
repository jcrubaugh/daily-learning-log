"""
API Pipeline - Basic API Call and Data Extraction
Fetches user data from a public REST API and prints contact info to the console.
"""

import requests
import json
import urllib3

# Suppress SSL verification warnings (common when verify=False is used)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the API endpoint — JSONPlaceholder is a free fake REST API for testing
url = "https://jsonplaceholder.typicode.com/users"

# Make a GET request to the API (SSL verification disabled for compatibility)
response = requests.get(url, verify=False)

# Parse the JSON response body into a Python list of dictionaries
data = response.json()

# Iterate through each user record and extract name + email for display
for user_info in data:
        name = user_info['name']
        email = user_info['email']
        print(f"User {name} can be reached at {email}")
