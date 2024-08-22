import requests
import os
from tools import download_image
import argparse


def main():
    parser = argparse.ArgumentParser(description='Download ID from SpaceX')
    parser.add_argument('--ID', type=str, help='Input ID of SpaceX launch photos', default='5eb87d47ffd86e000604b38a')
    args = parser.parse_args()

    url = f'https://api.spacexdata.com/v5/launches/{args.ID}'
    response = requests.get(url)
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        filename = f'images/spaceX{picture_number}.jpeg'           
        download_image(picture, filename)


if __name__ == "__main__":
    main()