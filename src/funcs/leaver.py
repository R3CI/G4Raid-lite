from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.discord import discord
from src.utils.stats import stats
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

class leaver:
    def __init__(self):
        self.console = console('Leaver')
        self.stats = stats('Leaver', [stats.SUCCEDED, stats.FAILED])
        self.serverid = None
    
    def leave(self, client: Client):
        try:
            while True:
                r = client.sess.delete(
                    f'https://discord.com/api/v9/users/@me/guilds/{self.serverid}',
                    headers=client.headers,
                    json={
                        'lurking': False
                    }
                )

                if r.status_code == 204:
                    logger.success(f'{client.maskedtoken} » Left')
                    self.stats.append(stats.SUCCEDED, client.token)
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

                elif 'You need to verify' in r.text:
                    logger.locked(f'{client.maskedtoken} Locked/Flagged')
                    self.stats.append(stats.FAILED, client.token, 'Locked/Flagged')
                    break

                else:
                    e, etype = discord.errordatabase(r.text) 
                    logger.error(f'{client.maskedtoken} » {e}')
                    self.stats.append(stats.FAILED, client.token, e)
                    break
                
        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.stats.append(stats.FAILED, client.token, e)

    def run(self, token):
        client = Client(token)
        self.leave(client)

    def menu(self):
        self.console.prep()
        self.serverid = self.console.input('Server ID', str)
        self.delay = self.console.input('Delay', float)
        logger.info(f'Stats will be saved to {self.stats.path}')

        threading(
            func=self.run,
            tokens=[token.token for token in files.gettokens()],
            delay=self.delay
        )

        
