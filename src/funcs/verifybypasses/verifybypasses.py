from src import *
from src.utils.console import console
from src.utils.printing import choicehandler

class verifybypasses:
    def __init__(self):
        self.console = console('Verify Bypasses')
    
    def reaction(self):
        choicehandler()

    def button(self):
        choicehandler()

    def rule(self):
        choicehandler()

    def onboarding(self):
        choicehandler()

    def restorecord(self):
        choicehandler()

    def authgg(self):
        choicehandler()

    def menu(self):
        menu = {
            'Reaction Bypass': self.reaction,
            'Button Bypass': self.button,
            'Rule Btpass': self.rule,
            'Onboarding Bypass': self.onboarding,
            'Restorecord Bypass': self.restorecord,
            'Authgg Bypass': self.authgg,
        }

        self.console.createmenu(menu)
        choice = self.console.input('Choice', int)
        choicehandler()