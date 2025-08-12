from src import *
from src.utils.config import get
from src.utils.files import files

class RPC:
    def __init__(self):
        try:
            smalltext = f'Tokens » {len(files.gettokens())} Proxies » {len(files.getproxies())}'
            self.client_id = '1383168674277363784'
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.rpc.update(
                state='discord.gg/spamming',
                details=f'G4Tools.TOP',
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

    def update(self, details):
        try:
            smalltext = f'Tokens » {len(files.gettokens())} Proxies » {len(files.getproxies())}'
            self.rpc.update(
                state=f'Simply the best',
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