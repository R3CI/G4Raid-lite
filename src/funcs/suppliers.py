from src import *
from src.utils.console import console

class suppliers:
    def __init__(self):
        self.console = console('Suppliers')

    def tokens(self):
        supp = requests.get('https://pastebin.com/raw/MdHKTEum').text
        webbrowser.open(supp)

    def proxies(self):
        supp = requests.get('https://pastebin.com/raw/HcRRZ0x1').text
        webbrowser.open(supp)
    
    def menu(self):
        menu = {
            'Tokens': self.tokens,
            'Proxies': self.proxies
        }

        self.console.createmenu(menu)
        choice = self.console.input('Choice', int)

        if choice == 1:
            self.tokens()

        elif choice == 2:
            self.proxies()