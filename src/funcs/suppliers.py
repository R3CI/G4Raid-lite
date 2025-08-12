# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged


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
