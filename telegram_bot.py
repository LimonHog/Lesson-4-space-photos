import telegram
from dotenv import load_dotenv
import os
import random
import time
import argparse


load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=bot_token)
chat_id="@download_photos"

bot.send_message(text='Кря', chat_id=chat_id)
# with open("images/spaceX1.jpg", 'rb') as photo_id:
#     bot.send_photo(chat_id=chat_id, photo=photo_id, timeout = 100)

parser = argparse.ArgumentParser(description='Отправляет случайное изобранеи в Телеграм')
parser.add_argument(
    '--frequence',
    type=int,
    default=14400,
    help='provide an integer (default: 14400)'
)
parser_period = parser.parse_args()

while True:
    for dirpath, dirnames, filenames in os.walk('images'):
     
        random.shuffle(filenames)
        bot.send_message(text=filenames[0], chat_id=chat_id)#не забудь исправит на вариант с изобр :3
#        with open(f"images/{filenames[0]}", 'rb') as photo_id:
#           bot.send_photo(chat_id=chat_id, photo=photo_id)
        time.sleep(2)
    time.sleep(parser_period.frequence)
    break

