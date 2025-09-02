from .base import BaseModule
from rubpy import Client,filters
from rubpy.types import Update
import asyncio

class WelcomeModule(BaseModule):


    def setup(self):
        
        self.filters.append( filters.regex('hello') )


    async def handler(self, update:Update):
        print('welcome')
        # if message.event_type == "join":
        #     message.reply("🎉 خوش اومدی به گروه!")


