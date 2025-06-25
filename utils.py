import os
import time
from dotenv import load_dotenv
import json

load_dotenv()

LOG_FILE = "logs.txt"
DATA_FILE = "data/iss_data.txt"

def log_action(action, status):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {action} - {status}\n")

def save_iss_data(label, data):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a") as f:
        f.write(f"\n[{timestamp}] {label}:\n{json.dumps(data, indent=2)}\n")
