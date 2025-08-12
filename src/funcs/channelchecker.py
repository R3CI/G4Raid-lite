from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.discord import discord
from src.utils.stats import stats
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

class channelchecker:
    def __init__(self):
        self.console = console('Channel Checker')
        self.stats = stats('Channel_Checker', [stats.SUCCEDED, stats.FAILED])
        self.channelid = None
    
    def check(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/channels/{self.channelid}',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Has access')
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

                else:
                    e, etype = discord.errordatabase(r.text) 
                    logger.error(f'{client.maskedtoken} » {e}')
                    self.stats.append(stats.FAILED, client.token, e)
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » Failed to check if as access » {e}')

    def run(self, token):
        client = Client(token)
        self.check(client)

    def menu(self):
        self.console.prep()
        self.channelid = self.console.input('Channel ID', str)
        self.delay = self.console.input('Delay', float)
        logger.info(f'Stats will be saved to {self.stats.path}')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')

        threading(
            func=self.run,
            tokens=[token.token for token in files.gettokens()],
            delay=self.delay
        )

        
