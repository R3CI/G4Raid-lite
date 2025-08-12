from src import *
from src.utils.console import console
from src.utils.logging import logger

class suppliers:
    def __init__(self):
        self.console = console('Suppliers')
        self.options = {
            'Tokens': self.tokens,
            'Proxies': self.proxies,
        }
        self.keys = list(self.options.keys())

    def tokens(self):
        options = {
            'Best overall recommended': webbrowser.open('https://www.tokenu.net?ref=r3ci'),
            'Second best (Deal with caution)': webbrowser.open('https://lzt.market/discord/'),
        }

        while True:
            self.console.printcustommenu(options)
            choice = self.console.input('Option', int) - 1

            if choice == len(self.keys):
                return
            
            elif choice < len(self.keys):
                self.options[self.keys[choice]]()
                break
            
            else:
                logger.info('Invalid choice')
                input('')

    def proxies(self):
        options = {
            'Best recommended': webbrowser.open('https://www.vital-proxies.com/?ref=m3dm062i'),
            'Second best': webbrowser.open('https://dataimpulse.com/?aff=171985'),
        }

        while True:
            self.console.printcustommenu(options)
            choice = self.console.input('Option', int) - 1

            if choice == len(self.keys):
                return
            
            elif choice < len(self.keys):
                self.options[self.keys[choice]]()
                break
            
            else:
                logger.info('Invalid choice')
                input('')

    def menu(self):
        while True:
            logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
            logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
            logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
            self.console.printcustommenu(self.options)
            choice = self.console.input('Option', int) - 1

            if choice == len(self.keys):
                return
            
            elif choice < len(self.keys):
                self.options[self.keys[choice]]()
                break
            
            else:
                logger.info('Invalid choice')
                input('')
