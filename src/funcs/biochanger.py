from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.discord import discord
from src.utils.config import get
from src.utils.printing import printing, choicehandler

class biochanger:
    def __init__(self):
        self.console = console('Bio Changer')
        self.bio = None

    def menu(self):
        self.console.prep()
        self.bio = self.console.input('Bio', str)
        choicehandler()

        
