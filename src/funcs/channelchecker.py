from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.printing import printing, choicehandler

class channelchecker:
    def __init__(self):
        self.console = console('Channel Checker')
        self.channelid = None

    def menu(self):
        self.console.prep()
        self.channelid = self.console.input('Channel ID', str)
        choicehandler()

        
