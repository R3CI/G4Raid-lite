from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.discord import discord
from src.utils.config import get
from src.utils.printing import choicehandler

class displaynamechanger:
    def __init__(self):
        self.console = console('Display Name Changer')
        self.name = None

    def menu(self):
        self.console.prep()
        self.name = self.console.input('Name', str)
        self.delay = self.console.input('Delay', float)
        choicehandler()

        
