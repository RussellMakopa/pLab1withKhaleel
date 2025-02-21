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


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def generate_short_id(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def is_valid_url(url):
    regex = re.compile(
    r'^(https://)?'
    r'([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}'
    r'(:[0-9]{1,5})?'
    )
    return re.match(regex, url)

def shorten_url(long_url):
    if not is_valid_url(long_url):
        return "Invalid URL: Please enter a valid URL"
    
    data = load_data()

    for short_id, url in data.items():
        if url == long_url:
            return BASE_URL + short_id
    
    short_id = generate_short_id()
    while short_id in data:
        short_id = generate_short_id()
        

