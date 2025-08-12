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
from src.utils.sessionmanager import client as Client, tokendata

class joiner:
    def __init__(self):
        self.console = console('Joiner')
        self.stats = stats('Joiner', [stats.SUCCEDED, stats.CAPTCHA, stats.FAILED])
        self.invite = None
        self.features = []

    def discover(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/invites/{self.invite}',
                    headers=client.headers,
                    params={
                        'inputValue': self.invite,
                        'with_counts': 'true',
                        'with_expiration': 'true',
                        'with_permissions': 'false',
                    },
                )

                if r.status_code == 200:
                    data = r.json()
                    guild = dict(data.get('guild', {}))
                    features = list(guild.get('features', []))
                    channel = dict(data.get('channel', {}))

                    self.serverid = guild.get('id')
                    self.servername = guild.get('name')
                    self.channelid = channel.get('id')
                    self.channeltype = channel.get('type')

                    if 'GUILD_ONBOARDING' in features:
                        if 'Onboarding' not in self.features:
                            self.features.append('Onboarding')

                    if 'MEMBER_VERIFICATION_GATE_ENABLED' in features:
                        if 'Rules' not in self.features:
                            self.features.append('Rules')

                    if 'AUTO_MODERATION' in features:
                        if 'AutoMod' not in self.features:
                            self.features.append('AutoMod')

                    if self.features:
                        extra = ','.join(self.features)
                    else:
                        extra = ''

                    logger.success(f'discord.gg/{self.invite} » {extra}')
                    return True

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
                    return False

                else:
                    e, etype = discord.errordatabase(r.text)
                    logger.error(f'{client.maskedtoken} » Failed to discover » {e}')
                    self.stats.append(stats.FAILED, client.token, e)
                    return False

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.stats.append(stats.FAILED, client.token, e) 
            return False

    def join(self, client: Client):
        # IT is this way cause of skiddies ;)
        try:
            while True:
                r = client.sess.post(
                    f'https://discord.com/api/v9/invites/{self.invite}',
                    headers=client.headers,
                    json={
                        'session_id': 'fdcf494d4663431db6cf19d52f8a4239'
                    },
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Joined {self.servername}')
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

                elif 'Unknown Message' in r.text:
                    logger.error(f'{client.maskedtoken} » Proxy/Token/Solver is FLAGGED')
                    self.stats.append(stats.FAILED, client.token, 'Proxy/Token/Solver is FLAGGED')
                    break

                elif 'captcha_key' in r.text:
                    logger.captcha(f'{client.maskedtoken} » Human verification required (COULD HAVE BEEN AVOIDED IF YOU WARE ON THE PAID VERSION)')
                    self.stats.append(stats.CAPTCHA, client.token)
                    break

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
        self.join(client)

    def menu(self):
        self.console.prep()
        self.invite = self.console.input('Invite', str)
        self.invite = discord.cleaninvite(self.invite)
        self.delay = self.console.input('Delay', float)
        logger.info(f'Stats will be saved to {self.stats.path}')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        tokens = [token.token for token in files.gettokens()]

        for token in tokens:
            client = Client(token)
            if self.discover(client):
                break

        if not self.servername:
            logger.error('Could not discover server')
            return

        threading(
            func=self.run,
            tokens=tokens,
            delay=self.delay,
        )

        if 'Onboarding' in self.features:
            bypassonbording = self.console.input('Bypass onboarding', bool)
            if bypassonbording:
                logger.info('This is a PAID ONLY feature buy paid on https://g4tools.top/g4spam')
                self.console.paidnotif()

        if 'Rules' in self.features:
            bypassrules = self.console.input('Bypass rules', bool)
            if bypassrules:
                logger.info('This is a PAID ONLY feature buy paid on https://g4tools.top/g4spam')
                self.console.paidnotif()