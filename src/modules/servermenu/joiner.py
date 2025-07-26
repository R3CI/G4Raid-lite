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

class joiner:
    def __init__(self):
        self.module = 'Joiner'
        self.logger = logger(self.module)
        self.ui = ui(self.module)
        self.invite = None

    def join(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            r = cl.sess.post(
                f'https://discord.com/api/v9/invites/{self.invite}',
                headers=cl.headers,
                json={
                    'session_id': cl.wssessid
                }
            )

            if r.status_code == 200:
                self.logger.succeded(f'{ctoken} Joined')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(float(limit))
                self.join(token, cl)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                time.sleep(5)
                self.join(token, cl)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                time.sleep(10)
                self.join(token, cl)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(f'{ctoken} Hcaptcha required (Could have been avoided with the paid version)')

            elif 'You need to verify' in r.text:
                self.logger.locked(f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(f'{ctoken}', error)

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def menu(self):
        self.ui.prep()
        self.logger.log('BETTER BYPASSING JOINER IN PAID ONLY!')
        self.logger.log('BETTER BYPASSING JOINER IN PAID ONLY!')
        self.logger.log('BETTER BYPASSING JOINER IN PAID ONLY!')
        self.invite = self.ui.input('Invite link', str)
        self.invite = discordutils.extractinv(self.invite)
        self.delay = self.ui.delayinput()

        threading(
            func=self.join,
            tokens=files.gettokens(),
            delay=self.delay,
        )