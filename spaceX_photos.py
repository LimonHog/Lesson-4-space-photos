import requests
import os
from dotenv import load_dotenv
from tools import download_image
import argparse


load_dotenv()
api_key = os.getenv('API_KEY')

parser = argparse.ArgumentParser(description='Download ID from SpaceX')
parser.add_argument('--ID', type=str, help='Input ID of SpaceX launch photos', default='5eb87d47ffd86e000604b38a')
args = parser.parse_args()


url = f'https://api.spacexdata.com/v5/launches/{args.ID}'
response = requests.get(url)
pictures = response.json()['links']['flickr']['original']
for picture_number, picture in enumerate(pictures):
    filename = f'images/spaceX{picture_number}.jpeg'
        
    download_image(picture, filename)

