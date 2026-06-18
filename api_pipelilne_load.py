"""
API Pipeline Day 11 - API Call with File Output
Fetches user data from a public REST API and writes a formatted directory
of users (name, company, email) to a text file.
"""

import requests
import json
import urllib3

# Suppress SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/users"

# Make a GET request to fetch all user records
response = requests.get(url, verify=False)

# Parse the JSON response into a Python list
data = response.json()

# Open an output file and write formatted user info line by line
with open("user_directory.txt", "w") as output_file:
        for user_info in data:
                # Extract relevant fields from each user record
                name = user_info['name']
                email = user_info['email']
                company_name = user_info['company']['name']

                # Write a formatted string for each user to the output file
                output_file.write(f"User {name} works at {company_name} and can be reached at {email}\n")
