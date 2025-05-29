import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches animal data from the API.
    Returns: list of animal dictionaries or empty list if error or no match.
    """
    if not API_KEY:
        print("Missing API Key in .env file.")
        return []

    headers = {"X-Api-Key": API_KEY}
    try:
        response = requests.get(API_URL, headers=headers, params={"name": animal_name})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return []