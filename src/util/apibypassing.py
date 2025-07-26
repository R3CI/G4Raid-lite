# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *

class apibypassing:
    def __init__(self):
        # Full api bypassing in paid only bc of skiddies 👍👍👍👍
        self.chromeversion = '136'
        self.fingerprint = f'chrome{self.chromeversion}'
        self.useragent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.chromeversion}.0.0.0 Safari/537.36'
        self.clientbuild = '423077'

        self.xsuper = {
            'os': 'Windows',
            'browser': 'Chrome',
            'device': '',
            'system_locale': 'en-US',
            'has_client_mods': False,
            'browser_user_agent': self.useragent,
            'browser_version': f'{self.chromeversion}.0.0.0',
            'os_version': '10',
            'referrer': None,
            'referring_domain': 'discord.com',
            'referrer_current': '',
            'referring_domain_current': '',
            'release_channel': 'stable',
            'client_build_number': self.clientbuild,
            'client_event_source': None,
            'client_launch_id': str(uuid.uuid4()), 
            'client_heartbeat_session_id': str(uuid.uuid4()),
            'client_app_state': 'focused'
        }
        self.headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua-platform': '"Windows"',
            'authorization': None,
            'x-debug-options': 'bugReporterEnabled',
            'sec-ch-ua': f'"Google Chrome";v="{self.chromeversion}", "Chromium";v="{self.chromeversion}", "Not/A)Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'x-discord-timezone': 'Europe/Warsaw',
            'x-super-properties': None,
            'x-discord-locale': 'en-US',
            'user-agent': self.useragent,
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': None,
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i'
        }
        

    def getcookie(self, headers, session: curlcffi.Session):
        # This doesnt grab ur acc cookies or wtv these cookies have no meaning and will not make me somehow have acces to ur acc using them as NOTHING is attached to them cookies are just needed for it to work good so please dont be a idiot (please be smart)
        r = session.get(
            'https://discord.com',
            headers=headers
        )

        return r.cookies
    
    def encode(self, data):
        return base64.b64encode(json.dumps(data, separators=(',', ':')).encode('utf-8')).decode('utf-8')
