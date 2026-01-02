from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.discord import discord
from src.utils.printing import printing, choicehandler

class channelspammer:
    def __init__(self):
        self.console = console('Channel Spammer')
        self.serverid = None
        self.channelid = None
        self.messages = []
        self.pingids = []
        self.dostring = False
        self.stringlen = 0
        self.doemoji = False
        self.emojilen = 0
        self.doping = False
        self.pinglen = 0
        self.tts = False
        self.delay = 0

    def menu(self):
        self.console.prep()
        self.serverid = self.console.input('Server ID', str)
        self.channelid = self.console.input('Channel ID', str)

        self.dostring = self.console.input('Add random a-z string? (e.g. abcde, randomized)', bool)
        if self.dostring:
            self.stringlen = self.console.input('How many letters? (e.g. 5 = 5 random letters)', int)

        self.doemoji = self.console.input('Add emojis like :thumbs_up:? (randomized)', bool)
        if self.doemoji:
            self.emojilen = self.console.input('How many emojis? (e.g. 3 = :emoji: :emoji2: :emoji3:)', int)

        self.doping = self.console.input('Add @user pings? (random users)', bool)
        if self.doping:
            pass

        self.messages = [self.console.input('Message', str)]

        self.tts = self.console.input('TTS', bool)
        choicehandler()
        
