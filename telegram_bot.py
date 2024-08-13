import telegram
from dotenv import load_dotenv
import os


load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=bot_token)
chat_id="@download_photos"

bot.send_message(text='Кря', chat_id=chat_id)
# with open("images/spaceX1.jpg", 'rb') as photo_id:
#     bot.send_photo(chat_id=chat_id, photo=photo_id, timeout = 100)

