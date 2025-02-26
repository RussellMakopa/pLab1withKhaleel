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
        r'^(https?://)?' 
        r'([a-zA-Z0-9.-]+)\.'  
        r'([a-zA-Z]{2,})' 
        r'(/\S*)?$' 
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

def get_original_url(short_url):
    data = load_data()
    short_id = short_url.split("/")[-1]
    return data.get(short_id, "URL not found")

def count_urls():
    data = load_data()
    return len(data)


def main():
    while True:
        choice = int (input("Enter your choice: "))

        if choice == 1:
            long_url = input ("Enter the full URL: ")
            print("The short URL", shorten_url(long_url))
        elif choice == 2:
            short_url = input("Enter the shortened URL: ")
            print("Original URL", get_original_url(short_url))
        elif choice == 3:
            print("Total URLs stored: ", count_urls())
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

        

