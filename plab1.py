import json
import string
import random
import re


DATA_FILE = "url_data.json"
BASE_URL = "http://www.short.com/"


def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}