import json

with open ("network_data.json") as file:
    data = json.load(file)
    for device_info in data:
        name = device_info['device']
        speed = device_info['uplink_gbps']
        print(f"Device {name} has a {speed} Gbps uplink")
