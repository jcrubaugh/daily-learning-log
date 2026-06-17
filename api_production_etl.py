import requests 
import json
import urllib3

# This line just hides the annoying "InsecureRequestWarning" text from flooding your terminal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"
response = requests.get(url, verify=False)


data = response.json()
filtered_users = []

for user_data in data:
        if user_data['language']=='Sindhi':
                myid = user_data['id']
                language = user_data['language']
                name = user_data['name']
                clean_record = {
                        "user_id" : myid,
                        'full_name' : name,
                        "spoken_language" : language
                                }
                filtered_users.append(clean_record)
with open ("production_metrics.json", "w") as outfile:
        json.dump(filtered_users, outfile, indent = 4)
