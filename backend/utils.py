# Import necessary modules and libraries

# Define utility functions
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Calculate distance between two coordinates
    R = 6371.0  # approximate radius of Earth in km

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def send_notification(device_id, message):
    # Send notification to a device
    print(f"Sending notification to device {device_id}: {message}")

# Add other utility functions as needed
