from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.discord import discord
from src.utils.config import get
from src.utils.printing import printing, choicehandler

class nicknamechanger:
    def __init__(self):
        self.console = console('Nickname Changer')
        self.nickname = None
        self.serverid = None
    def menu(self):
        self.console.prep()
        self.nickname = self.console.input('Nickname', str)
        self.serverid = self.console.input('Server ID', str)
        self.delay = self.console.input('Delay', float)
        choicehandler()

        
