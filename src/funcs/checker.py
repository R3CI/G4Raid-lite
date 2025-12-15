from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.logging import logger
from src.utils.discord import discord
from src.utils.sessionmanager import client as Client

def format_token(t):
    if t.email and t.password:
        return f'{t.email}:{t.password}:{t.token}'
    return t.token

class checker:
    def __init__(self):
        self.console = console('Checker')
        self.getinfo = False
        self.valids = []
        self.failed = []
        self.locked = []
        self.tokenmap = {}  # str(token) -> Token(email,password,token)

    def check(self, client: Client):
        tok = client.token
        token_obj = self.tokenmap.get(tok)
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/users/@me/library',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » MFA » ? EV » ? Email » ? Phone » ? Boosts » ? Age » ? days (get paid to see info)')
                    self.valids.append(token_obj)
                    break

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
                    if etype == discord.LOCKED_ACCOUNT:
                        self.locked.append(token_obj)
                    else:
                        self.failed.append(token_obj)
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.failed.append(token_obj)

    def run(self, token_obj):
        self.tokenmap[token_obj.token] = token_obj
        client = Client(token_obj.token)
        self.check(client)

    def menu(self):
        self.console.prep()
        self.delay = self.console.input('Delay', float)
        self.getinfo = self.console.input('Get all info and fully sort', bool)
        if self.getinfo:
            logger.info('Token sorting and info is anvaible in the paid version only')
            logger.info('Token sorting and info is anvaible in the paid version only')
            logger.info('Token sorting and info is anvaible in the paid version only')

        threading(
            func=self.run,
            tokens=files.gettokens(),
            delay=self.delay
        )
        
        replace = self.console.input('Replace tokens.txt with valid tokens ONLY', bool)
        if replace:
            with open('data\\tokens.txt', 'w', encoding='utf-8', errors='ignore') as f:
                f.write('\n'.join(format_token(t) for t in self.valids))
