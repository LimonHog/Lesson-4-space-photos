import requests
import os
from dotenv import load_dotenv


def download_image(url, filename, api_key=''):
    if not os.path.exists("images"):
        os.makedirs("images")
        
    params = {
        'api_key' : api_key,
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


load_dotenv()
api_key = os.getenv('API_KEY')

url = ' https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
response = requests.get(url)
pictures = response.json()['links']['flickr']['original']
for picture_number, picture in enumerate(pictures):
    filename = f'images/spaceX{picture_number}.jpeg'
        
    download_image(picture, filename)