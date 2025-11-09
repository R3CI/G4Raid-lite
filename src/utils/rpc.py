# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

from src import *
from src.utils.config import get
from src.utils.files import files

class RPC:
    def __init__(self):
        try:
            smalltext = f'Tokens » {len(files.gettokens())} Proxies » {len(files.getproxies())}'
            self.clientid = '1430609793436876820'
            self.rpc = Presence(self.clientid)
            self.rpc.connect()
            self.rpc.update(
                state='discord.gg/spamming',
                details='Using G4Raid',
                start=int(time.time()),
                large_image='smalllogorounded',
                large_text='discord.gg/spamming',
                small_image='folder',
                small_text=smalltext,
                buttons=[
                    {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                    {'label': 'Get G4Raid', 'url': 'https://g4tools.cc'}
                ]
            )
        except Exception as e:
            pass
    
    def update(self, details):
        try:
            smalltext = f'Tokens » {len(files.gettokens())} Proxies » {len(files.getproxies())}'
            self.rpc.update(
                state=details,
                details='Using G4FriendAdvertiser',
                start=int(time.time()),
                large_image='smalllogorounded',
                large_text='discord.gg/spamming',
                small_image='folder',
                small_text=smalltext,
                buttons=[
                    {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                    {'label': 'Get G4Raid', 'url': 'https://g4tools.cc'}
                ]
            )
        except Exception as e:
            pass

RPC = RPC()
