from core.bot import RubiBot
from modules import WelcomeModule,AntiSpamModule




def main():
    
    rubi = RubiBot()
    
    rubi.register_module(WelcomeModule())
    rubi.register_module(AntiSpamModule())

    rubi.run()




if __name__ == "__main__":
    main()
    

