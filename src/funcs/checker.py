from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.printing import printing, choicehandler
from src.utils.discord import discord

class checker:
    def __init__(self):
        self.console = console('Checker')

    def menu(self):
        self.console.prep()
        self.delay = self.console.input('Delay', float)
        self.getinfo = self.console.input('Get all info and fully sort', bool)
        choicehandler()
