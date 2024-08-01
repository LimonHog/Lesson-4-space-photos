import telegram
from dotenv import load_dotenv
import os


load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=bot_token)

updates = bot.get_updates()
bot.send_message(text='Кря', chat_id=1151243483)