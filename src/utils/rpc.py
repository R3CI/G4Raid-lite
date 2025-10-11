from src import *
from src.utils.config import get
from src.utils.files import files

class RPC:
    def __init__(self):
        self.rpc = None
        try:
            self.client_id = '1383168674277363784'
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.update('G4Tools.TOP')
        except:
            pass

    def update(self, details):
        if not self.rpc:
            return
            
        try:
            smalltext = f'Tokens » {len(files.gettokens())} Proxies » {len(files.getproxies())}'
            self.rpc.update(
                state='discord.gg/spamming',
                details=details,
                start=time.time(),
                large_image='smalllogorounded',
                large_text='discord.gg/spamming',
                small_image='folder',
                small_text=smalltext,
                buttons=[
                    {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                    {'label': 'Get G4Spam for FREE', 'url': 'https://github.com/R3CI/G4Spam'}
                ]
            )
        except:
            pass

RPC = RPC()