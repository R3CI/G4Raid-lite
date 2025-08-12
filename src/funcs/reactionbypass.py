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

class reactionbypass:
    def __init__(self):
        self.console = console('Reaction Bypass')
        self.stats = stats('Reaction_Bypass', [stats.SUCCEDED, stats.CAPTCHA, stats.FAILED])
        self.channelid = None
        self.serverid = None
        self.messageid = None
        self.url = None
        self.dodereact = False
        self.delay = 0
        self.reactions = []
    
    def getreactions(self, client: Client):
        try:
            while True:
                r = client.sess.get(
                    f'https://discord.com/api/v9/channels/{self.channelid}/messages?limit=50',
                    headers=client.headers
                )

                if r.status_code == 200:
                    logger.success(f'{client.maskedtoken} » Got reactions')
                    for message in r.json():
                        if message['id'] == self.messageid:
                            for reaction in message['reactions']:
                                if not message['reactions']:
                                    return self.reactions

                                emoji_name = reaction['emoji']['name']
                                emoji_id = reaction['emoji']['id']
                                count = reaction['count']
                                self.reactions.append((emoji_name, emoji_id, count))
                            
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
                    logger.error(f'{client.maskedtoken} » Failed to get reactions » {e}')
                    self.stats.append(stats.FAILED, client.token, e)
                    return False

        except Exception as e:
            logger.error(f'{client.maskedtoken} » Failed to get reactions » {e}')
            return False


    def react(self, client: Client):
        try:
            while True:
                r = client.sess.put(
                    self.url,
                    headers=client.headers
                )

                if r.status_code == 204:
                    logger.success(f'{client.maskedtoken} » Reacted')
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
                    self.stats.append(stats.FAILED, client.token, f'{e} - REACT')
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.stats.append(stats.FAILED, client.token, f'{e} - REACT')

    def dereact(self, client: Client):
        try:
            while True:
                r = client.sess.delete(
                    self.url,
                    headers=client.headers
                )

                if r.status_code == 204:
                    logger.success(f'{client.maskedtoken} » Dereacted')
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
                    self.stats.append(stats.FAILED, client.token, f'{e} - DEREACT')
                    break

        except Exception as e:
            logger.error(f'{client.maskedtoken} » {e}')
            self.stats.append(stats.FAILED, client.token, f'{e} - DEREACT')

    def run(self, token):
        client = Client(token)
        if self.dodereact:
            self.dereact(client)
        time.sleep(1)
        self.react(client)

    def menu(self):
        self.console.prep()
        self.serverid = self.console.input('Server ID', str)
        self.channelid = self.console.input('Channel ID', str)
        self.messageid = self.console.input('Message ID', str)
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')
        logger.info('GET BETTER BYPASSING AND BETTER WORKING VERSION BY BUYING PAID ON https://g4tools.top/g4spam')

        tokens = [token.token for token in files.gettokens()]
        for token in tokens:
            client = Client(token)
            if self.getreactions(client):
                break

        if not self.reactions:
            logger.error('No reactions found on that message')
            return

        menu = []
        for _, (reactionname, reactionid, count) in enumerate(self.reactions, 1):
            menu.append(f'{reactionname} » {count}')

        self.console.createmenu(menu)
        selected = self.console.input('Choice', int) - 1
        reaction = quote(self.reactions[selected][0], safe='')
        reactionid = self.reactions[selected][1]
        iscustom = reactionid is not None

        self.dodereact = self.console.input('DeReact (Set to yes if the reaction is currently reacted for the tokens)', bool)
        self.delay = self.console.input('Delay', float)
        logger.info(f'Stats will be saved to {self.stats.path}')

        if iscustom: self.url = f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{reaction}:{reactionid}/@me'
        else       : self.url = f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{reaction}/@me'

        threading(
            func=self.run,
            tokens=tokens,
            delay=self.delay
        )

        
