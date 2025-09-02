from rubpy import Client
from rubpy.types import Update

class BaseModule:

    def __init__(self):
        
        self.filters:list = []


    async def setup(self):
        pass


    async def handler(self, update:Update):
        pass


