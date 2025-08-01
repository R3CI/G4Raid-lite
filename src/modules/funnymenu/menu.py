from src import *
from src.util.logger import logger
from src.util.ui import ui

class funnymenu:
    def __init__(self):
        self.module = 'Funny Menu'
        self.logger = logger(self.module)
        self.ui = ui(self.module)

    def menu(self):
        options = {
            'Reaction Speller': lambda: self.ui.paidnotif(),
            'Audit Log Fucker': lambda: self.ui.paidnotif(),
            'Mass Caller': lambda: self.ui.paidnotif(),
        }
        
        while True:
            self.ui.optionmenu(options)
            choice = self.ui.input('Option', int) - 1
            keys = list(options.keys())
            
            if choice == len(keys):
                return
            
            elif choice < len(keys):
                options[keys[choice]]()
                break

            else:
                self.logger.log('Invalid option')
                input('')