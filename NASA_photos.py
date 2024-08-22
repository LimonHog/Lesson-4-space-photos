import requests
import os
from dotenv import load_dotenv
from tools import download_image


def get_extension(url):
    return os.path.splitext(url)[1]


def main():
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')

    params = {
            'api_key' : api_key,
            'count' : 30
        }
    
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    for picture_number, picture in enumerate(response.json()): 
        extension = get_extension(picture['url'])
        filename = f'images/nasa_apod{picture_number}{extension}'
        download_image(picture['url'], filename, api_key)


if __name__ == "__main__":
    main()