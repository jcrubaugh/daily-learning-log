import json


total_bandwidth = 0
with open ("network_data.json") as file:
    data = json.load(file)
    for device_info in data:
        name = device_info['device']
        speed = device_info['uplink_gbps']
        status = device_info['status']
        if device_info['status'] == 'active':
            total_bandwidth += speed

print(f"Total active uplink capacity: {total_bandwidth} Gbps")
