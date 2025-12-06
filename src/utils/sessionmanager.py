from src import *
from src.utils.files import files
from src.utils.config import get
from src.utils.logging import logger
tokendata = {}

# NOT FULL CAUSE I DONT WANT TO LEAK IT AND GET SKIDS TO USE ITTT   
class responsewrapper:
    def __init__(self, response=None, error=None):
        if response:
            self._response = response
            self.status_code = response.status_code
            self.headers = dict(response.headers) if response.headers else {}
            self.text = response.text
            self.cookies = response.cookies
            self.error = None
        else:
            self._response = None
            self.status_code = 0
            self.headers = {}
            self.text = str(error) if error else 'Error'
            self.cookies = None
            self.error = error

        logger.debug(f'Status » {self.status_code}')
        logger.debug(f'Headers » {self.headers}')
        logger.debug(f'Text » {self.text}')
        logger.debug(f'Error » {self.error}')
    
    def json(self) -> dict:
        if self.error:
            logger.debug(f'Failed to parse JSON » {self.error}')
            return {}
            
        try:
            return self._response.json()
        
        except Exception as e:
            logger.debug(f'Failed to parse JSON » {e}')
            return {}

class sessionwrapper:
    def __init__(self, impersonate=None):
        self.session = curlcffi.Session(
            impersonate=impersonate,
            timeout=15
        )
        self.cookies = self.session.cookies
        self.headers = dict(self.session.headers) if self.session.headers else {}
        
    def adddata(self, kwargs):
        headers = kwargs.get('headers', {})
        if 'json' in kwargs:
            payload = kwargs.pop('json')
            json_str = json.dumps(payload, separators=(',', ':'), ensure_ascii=False)
            kwargs['data'] = json_str.encode('utf-8')
            headers['Content-Type'] = 'application/json; charset=utf-8'
        elif 'data' in kwargs and kwargs['data'] is not None:
            data = kwargs['data']
            if isinstance(data, str):
                kwargs['data'] = data.encode('utf-8')
        if headers:
            kwargs['headers'] = headers
        return kwargs
   
    def request(self, method, url, **kwargs):
        headers = dict(kwargs.get('headers', {})) if kwargs.get('headers') else {}
        kwargs['headers'] = headers
        kwargs = self.adddata(kwargs)
        r = self.session.request(method, url, **kwargs)
        return responsewrapper(r)
            
    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)
    
    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)
    
    def put(self, url, **kwargs):
        return self.request('PUT', url, **kwargs)
   
    def patch(self, url, **kwargs):
        return self.request('PATCH', url, **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)


class curlwrapper:
    def Session(impersonate=None):
        return sessionwrapper(impersonate=impersonate)

class apibypassing_:
    # Before u complain its like this cause of skids lol
    def __init__(self):
        logger.info('Initializing API bypassing', 'API')
        self.cffiversion = 'chrome136'
        self.chromeversion = '140'
        self.fullchromeversion = '140.0.0.0'
        self.buildnumber = '476179' # not leaking the api bru
        self.useragent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.fullchromeversion} Safari/537.36'

        self.xsuper = {
            'os': 'Windows',
            'browser': 'Chrome',
            'device': '',
            'system_locale': 'en-US',
            'has_client_mods': False,
            'browser_user_agent': self.useragent,
            'browser_version': self.fullchromeversion,
            'os_version': '10',
            'referrer': None,
            'referring_domain': 'discord.com',
            'referrer_current': '',
            'referring_domain_current': '',
            'release_channel': 'stable',
            'client_build_number': int(self.buildnumber),
            'client_app_state': 'focused'
        }

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

    def getcookie(self, headers, session: curlcffi.Session):
        r = requests.get('https://discord.com', headers=headers)
        r.cookies.set('locale', 'en-GB', domain='.discord.com', path='/')
        return r.cookies, '; '.join([f'{cookie.name}={cookie.value}' for cookie in r.cookies])

    def encode(self, data):
        return base64.b64encode(json.dumps(data, separators=(',', ':')).encode('utf-8')).decode('utf-8')
apibypassing = apibypassing_()

class client:
    # Before u complain its like this cause of skids lol
    def __init__(self, token=None):
        self.token = token
        self.maskedtoken = token[:30] if token else None

        self.launchsignature = tokendata[token]['launchsignature']
        self.launchid = tokendata[token]['launchid']
        self.wssessid = tokendata[token]['wssessid']
        self.cookiejar = tokendata[token]['cookiejar']
        self.cookiestr = tokendata[token]['cookiestr']

        self.sess = self.makesess()
        self.xsuper = copy.deepcopy(apibypassing.xsuper)
        self.headers = copy.deepcopy(apibypassing.headers)
        self.settoken(token)
        self.addxsup(apibypassing.encode(self.xsuper))

    def makesess(self):
        return curlwrapper.Session(impersonate=apibypassing.cffiversion)

    def refreshcookies(self):
        self.cookiejar, self.cookiestr = apibypassing.getcookie(self.headers, self.sess)
        self.updatecookies(self.cookiejar, self.cookiestr)
        tokendata[self.token]['cookiejar'] = self.cookiejar
        tokendata[self.token]['cookiestr'] = self.cookiestr

    def updatecookies(self, cookiejar, cookiestr):
        if not self.cookiejar:
            logger.debug(f'{self.maskedtoken} » Getting cookies')
            self.cookiejar, self.cookiestr = apibypassing.getcookie(self.headers, self.sess)
            
        self.headers['cookie'] = cookiestr
        self.sess.cookies.update(cookiejar)
        tokendata[self.token]['cookiejar'] = self.cookiejar
        tokendata[self.token]['cookiestr'] = self.cookiestr

    def settoken(self, token):
        if token:
            self.headers['authorization'] = token

    def addxsup(self, xsuper):
        self.headers['x-super-properties'] = xsuper

    def addxcontent(self, xcontent):
        self.headers['x-context-properties'] = apibypassing.encode(xcontent)

    def cleanxcontent(self):
        self.headers = dict(self.headers)
        if self.headers.get('x-context-properties'):
            del self.headers['x-context-properties']
    
logger.info('Fetching discord related stuff', 'API')
for token in files.gettokens():
    tokendata[token.token] = {
        'cookiejar': None,
        'cookiestr': None
    }