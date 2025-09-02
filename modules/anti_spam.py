from .base import BaseModule
from rubpy import Client, filters
from rubpy.types import Update
import re
import asyncio

class AntiSpamModule(BaseModule):

    def __init__(self):
        super().__init__()

        self.bad_words = {"فحش۱", "فحش۲"}
        self.link_pattern = re.compile(r"(https?://|www\.)")
        self.repeated_messages = {}
        

    def setup(self):
    
        self.filters.append( filters.regex('spam') )

                
    async def handler(self, update:Update):
        print('anti-spam')
        # print(message.text)
        # user_id = message.sender_id
        # text = message.text.strip()
        
        # # بررسی لینک
        # if self.link_pattern.search(text):
        #     self.bot.delete_message(message.chat_id, message.message_id)
        #     self.bot.send_message(message.chat_id, "🚫 ارسال لینک مجاز نیست.")
        #     return

        # # بررسی فحاشی
        # if any(word in text for word in self.bad_words):
        #     self.bot.delete_message(message.chat_id, message.message_id)
        #     self.bot.send_message(message.chat_id, "⚠️ لطفاً ادب رو رعایت کن.")
        #     return

        # # بررسی پیام‌های تکراری
        # if user_id in self.repeated_messages and self.repeated_messages[user_id] == text:
        #     self.bot.delete_message(message.chat_id, message.message_id)
        #     self.bot.send_message(message.chat_id, "⛔ لطفاً از ارسال پیام‌های تکراری خودداری کنید.")
        #     return

        # self.repeated_messages[user_id] = text
