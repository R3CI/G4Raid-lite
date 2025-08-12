# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.discord import discord
from src.utils.stats import stats
from src.utils.logging import logger
from src.utils.sessionmanager import client as Client

class serverchecker:
    def __init__(self):
        self.console = console('Server Checker')
        self.stats = stats('Server_Checker', [stats.SUCCEDED, stats.FAILED])
        self.serverid = None
    
    def check(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/guilds/{self.serverid}',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Inside')
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
        self.check(client)

    def menu(self):
        self.console.prep()
        self.serverid = self.console.input('Server ID', str)
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

        
