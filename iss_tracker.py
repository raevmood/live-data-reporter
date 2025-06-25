import requests
import time
from utils import log_action, save_iss_data

ISS_API = "http://api.open-notify.org/iss-now.json"

def track_iss():
    try:
        response = requests.get(ISS_API)
        response.raise_for_status()
        data = response.json()
        position = data["iss_position"]

        print(f"\nISS Current Location:")
        print(f"Latitude: {position['latitude']}, Longitude: {position['longitude']}")

        save_iss_data("ISS Position", position)
        log_action("ISS position fetched", "Success")
    except Exception as e:
        log_action("ISS position fetch", f"Failed: {e}")
        print(f"Error: {e}")