from src import *
from src.utils.logging import logger
tokendata = {}

class responsewrapper:
    # Full wrapper on PAID bc of skids!
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
            timeout=10
        )
        self._proxies = None
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

class apibypassing:
    def __init__(self): 
        # FULL API BYPASSING IN PAID ONLY BC OF SKIDDDIEESSSSS
        logger.info('Initializing API bypassing', 'API')
        self.fullchromeversion = f'136.0.0.0'
        self.fingerprint = f'chrome136'
        self.clientbuild = 429117
        self.useragent = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{self.fullchromeversion} Safari/537.36'
        # Before you comment on this it is done like that cause of skiddies ;)
        self.headers = {
            'authorization': None,
            'x-discord-locale': 'en-US',
            'user-agent': self.useragent,
            'content-type': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
        }
    
    def getcookie(self, headers, session: curlcffi.Session):
        r = session.get(
            'https://discord.com',
            headers=headers
        )
        return r.cookies
apibypassing = apibypassing()

class client:
    def __init__(self, token=None,):
        self.token = token
        self.headers = copy.deepcopy(apibypassing.headers)
        self.maskedtoken = token[:30] if token else None
        self.sess = self.makesess()
        self.updatecookies(cookie)
        self.settoken(token)

    def makesess(self):
        return curlwrapper.Session(impersonate=apibypassing.fingerprint)
   
    def updatecookies(self, cookie):
        self.sess.cookies.update(cookie)

    def settoken(self, token):
        if token:
            self.headers['authorization'] = token

logger.info('Fetching discord related stuff', 'API')

logger.info(f'Fingerprint » {apibypassing.fingerprint}', 'API')
logger.info(f'Client build » {apibypassing.clientbuild}', 'API')

tempsess = curlwrapper.Session(impersonate=apibypassing.fingerprint)
cookie = apibypassing.getcookie(apibypassing.headers, tempsess)

logger.info(f'Fetching discord related stuff', 'API')