import requests
import os
from dotenv import load_dotenv
from tools import download_image



load_dotenv()
api_key = os.getenv('API_KEY')

url = ' https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
response = requests.get(url)
pictures = response.json()['links']['flickr']['original']
for picture_number, picture in enumerate(pictures):
    filename = f'images/spaceX{picture_number}.jpeg'
        
    download_image(picture, filename)