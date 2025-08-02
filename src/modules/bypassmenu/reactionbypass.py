# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam


from src import *
from src.util.logger import logger
from src.util.client import client
from src.util.ui import ui
from src.util.apibypassing import apibypassing
from src.util.discordutils import discordutils
from src.util.threading import threading
from src.util.files import files
apibypassing = apibypassing()

class reactionbypass:
    def __init__(self):
        self.module = 'Reaction bypass'
        self.logger = logger(self.module)
        self.ui = ui(self.module)
        
        self.url = None
        self.serverid = None
        self.channelid = None
        self.messageid = None
        self.delay = 0

    def react(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            r = cl.sess.put(
                self.url,
                headers=cl.headers,
                params={
                    'location': 'Message Hover Bar'
                }
            )

            if r.status_code == 204:
                self.logger.succeded(f'{ctoken} Reacted')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(float(limit))
                self.react(token, cl)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                time.sleep(5)
                self.react(token, cl)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                time.sleep(10)
                self.react(token, cl)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(f'{ctoken} Hcaptcha required')

            elif 'You need to verify' in r.text:
                self.logger.locked(f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(f'{ctoken}', error)

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def dereact(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            r = cl.sess.delete(
                self.url,
                headers=cl.headers
            )

            if r.status_code == 204:
                self.logger.succeded(f'{ctoken} DeReacted')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(float(limit))
                self.react(token, cl)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                time.sleep(5)
                self.react(token, cl)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                time.sleep(10)
                self.react(token, cl)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(f'{ctoken} Hcaptcha required')

            elif 'You need to verify' in r.text:
                self.logger.locked(f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(f'{ctoken}', error)

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def menu(self):
        self.ui.prep()
        reactionmessage = self.ui.input('Message Link', str)
        ids = discordutils.extractids(reactionmessage)
        self.serverid = ids['server']
        self.channelid = ids['channel']
        self.messageid = ids['message']

        self.dodereact = self.ui.input('DeReact (if they reacted before so it registers for the bot again)', bool)
        self.delay = self.ui.delayinput()

        reactions = discordutils.getreactions(files.gettokens(), self.channelid, self.messageid)
        if not reactions:
            self.logger.log('No reactions found on that message')
            return

        menu = []
        for _, (reactionname, emoji_id, count) in enumerate(reactions, 1):
            menu.append(f'{reactionname} » {count}')
        self.ui.createmenu(menu)
        selected = int(self.ui.input('Choice', str)) - 1
        reaction = reactions[selected][0]
        reactionid = reactions[selected][1]
        iscustom = reactionid is not None

        if iscustom: self.url = f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{reaction}:{reactionid}/@me'
        else       : self.url = f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{reaction}/@me'

        if self.dodereact:
            threading(
                func=self.dereact,
                tokens=files.gettokens(),
                delay=self.delay,
            )

        threading(
            func=self.react,
            tokens=files.gettokens(),
            delay=self.delay,
        )