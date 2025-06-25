import requests
import time
from utils import log_action, save_iss_data

ASTRONAUTS_API = "http://api.open-notify.org/astros.json"

def fetch_astronauts():
    try:
        response = requests.get(ASTRONAUTS_API)
        response.raise_for_status()
        data = response.json()

        print("\nPeople currently in space:")
        for person in data["people"]:
            print(f"- {person['name']} aboard {person['craft']}")

        save_iss_data("Astronauts", data["people"])
        log_action("Astronauts fetched", "Success")
    except Exception as e:
        log_action("Astronauts fetch", f"Failed: {e}")
        print(f"Error: {e}")
