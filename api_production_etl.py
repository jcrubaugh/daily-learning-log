"""
Production ETL - API Extract, Filter, Transform, and Load
Pulls dummy user data from a public API, filters for Sindhi speakers,
transforms into a clean schema, and writes the result to a JSON file.
"""

import requests
import json
import urllib3

# Suppress SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the API endpoint — Microsoft Edge demo dataset with user profiles
url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"

# EXTRACT: Fetch raw data from the API
response = requests.get(url, verify=False)

# Parse the full JSON response into a list of user records
data = response.json()

# TRANSFORM: Filter and reshape the data
filtered_users = []

for user_data in data:
        # Only keep users whose language is 'Sindhi'
        if user_data['language'] == 'Sindhi':
                myid = user_data['id']
                language = user_data['language']
                name = user_data['name']

                # Build a clean, standardized record with renamed fields
                clean_record = {
                        "user_id": myid,
                        'full_name': name,
                        "spoken_language": language
                }
                filtered_users.append(clean_record)

# LOAD: Write the filtered data to a JSON output file (pretty-printed)
with open("production_metrics.json", "w") as outfile:
        json.dump(filtered_users, outfile, indent=4)
