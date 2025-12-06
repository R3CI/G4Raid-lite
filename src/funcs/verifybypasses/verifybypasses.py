from src import *
from src.utils.console import console
from src.utils.logging import logger

class verifybypasses:
    def __init__(self):
        self.console = console('Verify Bypasses')
    
    def reaction(self):
        logger.paidonly()

    def button(self):
        logger.paidonly()

    def rule(self):
        logger.paidonly()

    def onboarding(self):
        logger.paidonly()

    def restorecord(self):
        logger.paidonly()

    def authgg(self):
        logger.paidonly()

    def menu(self):
        menu = {
            'Reaction Bypass $': self.reaction,
            'Button Bypass $': self.button,
            'Rule Btpass $': self.rule,
            'Onboarding Bypass $': self.onboarding,
            'Restorecord Bypass $': self.restorecord,
            'Authgg Bypass $': self.authgg,
        }

        self.console.createmenu(menu)
        choice = self.console.input('Choice', int)

        if choice == 1:
            self.reaction()

        elif choice == 2:
            self.button()

        elif choice == 3:
            self.rule()

        elif choice == 4:
            self.onboarding()

        elif choice == 5:
            self.restorecord()
        
        elif choice == 6:
            self.authgg()