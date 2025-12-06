from src import *
from src.utils.config import get
from src.utils.files import files

class RPC:
    def __init__(self):
        try:
            if get.rpc.enabled():
                if get.rpc.showdata():
                    smalltext = f'Tokens » {len(files.gettokens())} Proxies » 0'
                else:
                    smalltext = f'Tokens » Private | Proxies » Private'
                self.clientid = '1430609793436876820'
                self.rpc = Presence(self.clientid)
                self.rpc.connect()
                self.rpc.update(
                    state='discord.gg/spamming',
                    details='Using G4Raid-lite',
                    start=int(time.time()),
                    large_image='smalllogorounded',
                    large_text='discord.gg/spamming',
                    small_image='folder',
                    small_text=smalltext,
                    buttons=[
                        {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                        {'label': 'Get G4Raid for FREE', 'url': 'https://github.com/r3ci/G4Raid'}
                    ]
                )
        except Exception as e:
            pass
    
    def update(self, details):
        try:
            if get.rpc.enabled():
                if get.rpc.showdata():
                    smalltext = f'Tokens » {len(files.gettokens())} Proxies » 0'
                else:
                    smalltext = f'Tokens » Private | Proxies » Private'
                self.rpc.update(
                    state=details,
                    details='Using G4Raid-lite',
                    start=int(time.time()),
                    large_image='smalllogorounded',
                    large_text='discord.gg/spamming',
                    small_image='folder',
                    small_text=smalltext,
                    buttons=[
                        {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                        {'label': 'Get G4Raid for FREE', 'url': 'https://github.com/r3ci/G4Raid'}
                    ]
                )
        except Exception as e:
            pass

RPC = RPC()