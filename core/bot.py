from utils.config_loader import load_config
from modules.base import BaseModule
from rubpy import Client,filters
from rubpy.types import Update


class RubiBot:
    def __init__(self):
        config = load_config()
        self.client = Client(name="config/Soheil", auth=config['auth'], private_key=config['key'])        
        self.modules:list[BaseModule] = []




    def register_module(self, module):        
        self.modules.append(module)



    def run(self):  

        for module in self.modules:
            module.setup()
            m_filters = module.filters

            def make_handler(m):
                @self.client.on_message_updates(*m_filters)
                async def handle_message(*args,**kwargs):
                    await m.handler(*args,**kwargs)
                return handle_message

            make_handler(module)


        self.client.run()


