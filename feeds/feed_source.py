import requests
from bs4 import BeautifulSoup
import config


def get_phishtank_feed():
    url = config.phishtank_url
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error Phishtank feed. Status code: {response.status_code}")
        return []

