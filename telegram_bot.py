import telegram
from dotenv import load_dotenv
import os


load_dotenv()
bot_token = os.getenv('TELEGRAM_TOKEN')
bot = telegram.Bot(token=bot_token)

print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

updates = bot.get_updates()
bot.send_message(text='Кря', chat_id=-1002162061613)