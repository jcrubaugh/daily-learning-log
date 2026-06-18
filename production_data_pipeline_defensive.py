import requests
import json
import urllib3

# Suppress SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the API endpoint — Microsoft Edge demo dataset with user profiles
url = "https://microsoftedge.github.io/Demos/json-dummy-data/64KB.json"

def production_data_pipeline(target_language, output_filename):
    # EXTRACT: Fetch raw data from the API
    response = requests.get(url, verify=False)

    # Parse the full JSON response into a list of user records
    data = response.json()

    # TRANSFORM: Filter and reshape the data
    filtered_users = []

    for user_data in data:
            # Only keep users whose language is 'Sindhi'
            if user_data.get('language') == target_language :
                    myid = user_data.get('id', 'unknown-id')
                    language = user_data.get('language', 'unknown-language')
                    name = user_data.get('name', 'unknown-name')

                    # Build a clean, standardized record with renamed fields
                    clean_record = {
                            "user_id": myid,
                            'full_name': name,
                            "spoken_language": language
                    }
                    filtered_users.append(clean_record)

    # SORT: Order the filtered records by full_name in descending (Z-A) order
    sorted_users = sorted(filtered_users, key=lambda clean_record: clean_record['full_name'], reverse=True)

    # LOAD: Write the sorted, filtered data to a JSON output file
    with open(output_filename, "w") as outfile:
            json.dump(sorted_users, outfile, indent=4)

# Execution 1: Extract and sort Sindhi profiles
production_data_pipeline("Sindhi", "sindhi_profiles.json")

# Execution 2: Extract and sort Swedish profiles
production_data_pipeline("Uyghur", "uyghur_profiles.json")
