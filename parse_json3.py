import json


def run_bandwidth_pipeline():

    total_bandwidth = 0
    try:

        with open ("network_data.json") as file:
            data = json.load(file)
            for device_info in data:
                name = device_info['device']
                speed = device_info['uplink_gbps']
                status = device_info['status']
                if device_info['status'] == 'active':
                    total_bandwidth += speed

        print(f"Total active uplink capacity: {total_bandwidth} Gbps")

    except FileNotFoundError:
        print(f"[ERROR]: The file network_data.json could not be found. Please check the filepath.")

run_bandwidth_pipeline()


