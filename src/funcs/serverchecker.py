from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.discord import discord
from src.utils.printing import printing, choicehandler

class serverchecker:
    def __init__(self):
        self.console = console('Server Checker')
        self.serverid = None

    def menu(self):
        self.console.prep()
        self.serverid = self.console.input('Server ID', str)
        self.delay = self.console.input('Delay', float)
        choicehandler()

        
