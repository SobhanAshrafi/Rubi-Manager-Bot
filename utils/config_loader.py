import json
from dotenv import load_dotenv
import os

def load_config():
    load_dotenv('config/secrets.env')
    with open("config/settings.json", "r", encoding="utf-8") as f:
        settings = json.load(f)
    settings["auth"] = os.getenv("AUTH")
    settings["key"] = os.getenv("KEY")

    return settings
