import requests 
import json
import urllib3

# This line just hides the annoying "InsecureRequestWarning" text from flooding your terminal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, verify=False)


data = response.json()

for user_info in data:
        name = user_info['name']
        email = user_info['email']
        company_name = user_info['company']['name']
        print(f"User {name} works at {company_name} and can be reached at {email}")
