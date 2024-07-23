import requests
import os
import datetime
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

#here u're "cikle" start
params = {
    'api_key' : api_key
}

for i in range(10):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=params)
    epic_image = response.json()[i]['image']
    
    date = response.json()[0]['date']
    date = date.split()
    date = date[0].split('-')
    
    planet_url = f"https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{epic_image}.png?"
    
    download_image(planet_url, f'images/epic_photo{i}.png', api_key)