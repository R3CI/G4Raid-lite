from src import *
from src.utils.console import console
from src.utils.logging import logger

class suppliers:
    def __init__(self):
        self.console = console('Suppliers')

    def tokens(self):
        supp = requests.get('https://g4tools.cc/api/tokensupplier').text
        logger.info('IMPORTANT > AFTER BUYING THEM WAIT 1-2 DAYS BEFORE USE YES EVEN WITH AGED ONES', 'Suppliers')
        logger.info(f'Tokens are available at {supp}', 'Suppliers')
        webbrowser.open(supp)

    def proxies(self):
        supp = requests.get('https://g4tools.cc/api/proxysupplier').text
        logger.info(f'Proxies are available at {supp}', 'Suppliers')
        webbrowser.open(supp)
    
    def menu(self):
        menu = {
            'Tokens': self.tokens,
            'Proxies (BUY RESIDENTIAL ONLY)': self.proxies
        }

        self.console.createmenu(menu)
        choice = self.console.input('Choice', int)

        if choice == 1:
            self.tokens()

        elif choice == 2:
            self.proxies()