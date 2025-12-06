from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.discord import discord
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

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
    
    def spam(self, client: Client):
        try:
            client.cleanxcontent()
            client.addxcontent({
                'location': 'chat_input'
            })
            if not client.cookiejar:
                logger.infolog(f'{client.maskedtoken} » Getting cookies')
                client.refreshcookies()
                client.updatecookies(client.cookiejar, client.cookiestr)

            while True:
                message = random.choice(self.messages)

                if self.dostring:
                    message = f'{message} | {discord.getstring(self.stringlen)}'

                if self.doemoji:
                    message = f'{message} | {discord.getemoji(self.emojilen)}'

                r = client.sess.post(
                    f'https://discord.com/api/v9/channels/{self.channelid}/messages',
                    headers=client.headers,
                    json={
                        'mobile_network_type': 'unknown',
                        'content': f'# https://g4tools.cc\n{message}',
                        'nonce': discord.getnonce(),
                        'flags': 0
                    }
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Sent')

                elif 'retry_after' in r.text:
                    ratelimit = r.json().get('retry_after', 1.5)
                    logger.ratelimit(f'{client.maskedtoken} » {ratelimit}s')
                    discord.sleep(ratelimit)

                elif 'Try again later' in r.text:
                    logger.ratelimit(f'{client.maskedtoken} » 5s')
                    discord.sleep(5)

                elif 'Cloudflare' in r.text:
                    logger.cloudflare(f'{client.maskedtoken} » 10s')
                    discord.sleep(10)

                else:
                    e, etype = discord.errordatabase(r.text) 
                    logger.error(f'{client.maskedtoken} » {e}')
                    break
                    
                discord.sleep(self.delay)

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')

    def run(self, token):
        client = Client(token)
        self.spam(client)

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
            logger.info('Pings are anvaible in the paid version only')
            logger.info('Pings are anvaible in the paid version only')
            logger.info('Pings are anvaible in the paid version only')

        if self.console.input('Use messages from a file', bool):
            logger.info('Choose the file with ur messages');time.sleep(1)
            path = files.choosefile()
            if not os.path.exists(path):
                logger.error('This file does not exist')
                self.messages = [self.console.input('Message', str)]

            else:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    self.messages = f.read().splitlines()
        else:
            self.messages = [self.console.input('Message', str)]

        self.tts = self.console.input('TTS', bool)
        self.delay = self.console.input('Delay', float)
        logger.info('No watermark is anvaible in the paid version only')
        logger.info('No watermark is anvaible in the paid version only')
        logger.info('No watermark is anvaible in the paid version only')

        tokens = [token.token for token in files.gettokens()]
            
        threading(
            func=self.run,
            tokens=tokens,
            delay=0
        )

        
