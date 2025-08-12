from src import *
from src.utils.files import files
from src.utils.console import console
from src.utils.threading import threading
from src.utils.logging import logger
from src.utils.discord import discord
from src.utils.sessionmanager import client as Client

class checker:
    def __init__(self):
        self.console = console('Checker')
        os.makedirs('data\\invitechecker', exist_ok=True)
        timestamp = dt.now().strftime('%Y-%m-%d--%H-%M-%S')
        self.sortingpath = 'data\\tokenchecker\\' + timestamp
        self.getinfo = False
        self.valids = []
        self.failed = []

    def check(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/users/@me/library',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Valid')
                    self.valids.append(client.token)
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
                    self.failed.append(client.token)
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.failed.append(client.token)

    def run(self, token):
        client = Client(token)
        self.check(client)

    def menu(self):
        self.console.prep()
        self.delay = self.console.input('Delay', float)
        self.getinfo = self.console.input('Get all info and fully sort', bool)
        if self.getinfo:
            logger.info('GET INFO is a PAID ONLY feature buy paid on https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')

        threading(
            func=self.run,
            tokens=[token.token for token in files.gettokens()],
            delay=self.delay
        )

        os.makedirs(self.sortingpath, exist_ok=True)
        valids_path = self.sortingpath + '\\valids.txt'
        with open(valids_path, 'w') as f:
            f.write('\n'.join(self.valids))

        failed_path = self.sortingpath + '\\failed-invalid.txt'
        with open(failed_path, 'w') as f:
            f.write('\n'.join(self.failed))