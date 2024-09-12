import requests
import os
import datetime
from dotenv import load_dotenv
from tools import download_image


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']

    params = {
        'api_key' : api_key
    }
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    earth_change_info = response.json()

    for image_number, image in enumerate(earth_change_info):

        epic_image = image['image']
        
        date = earth_change_info[0]['date']
        date = date.split()
        date = date[0].split('-')
        
        planet_url = f"https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{epic_image}.png?"
        
        download_image(planet_url,  os.path.join('images', f'epic_photo{image_number}.png'), api_key)
       
if __name__ == "__main__":
    main()