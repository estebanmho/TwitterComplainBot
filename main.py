import time
import os
from internetSpeedTwitterBot import InternetSpeedTwitterBot
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()


