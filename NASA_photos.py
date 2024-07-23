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


def get_extension(url):
    return os.path.splitext(url)[1]


load_dotenv()
api_key = os.getenv('API_KEY')

params = {
        'api_key' : api_key,
        'count' : 30
    }
response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
for picture_number, picture in enumerate(response.json()): 
    extension = get_extension(picture['url'])
    filename = f'images/nasa_apod{picture_number}{extension}'
    download_image(picture['url'], filename, api_key)



