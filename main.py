# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

import sys
sys.dont_write_bytecode = True

from src import *
from src.util.autoupdate import autoupdate; autoupdate().update()
from src.util.client import *
from src.util.ui import ui
from src.util.rpc import RPC
from src.util.logger import logger
from src.util.other import other
from src.util.files import files; files.runtasks()
from src.util.config import config; config()
from src.modules import *
logger = logger('Main')
sui = ui('Main') 

logger.log('Adding a launch to stats', True)
other.addlaunch()

logger.log('Getting repo stars...', True)
stars = other.getrepostars()

logger.log('Getting launches...', True)
launches = other.getlaunches()

logger.log('Checking config...', True)
config().check()

logger.log(f'Connecting tokens is PAID only, this will result in bit worse bypassing', True)

logger.log('Finished starting G4Spam', True)

while True:
    RPC.update('In main menu')
    sui.title(f'G4Spam FREE ({launches}) - github.com/R3CI/G4Spam ({stars}) - discord.gg/spamming - Made by r3ci')
    sui.cls()
    sui.banner()
    sui.bar()
    sui.menu()

    logger.log('Welcome to G4Spam made by r3ci <3 github.com/R3CI/G4Spam')
    logger.log(f'Get FULL version on https://g4tools.top')
    logger.log(f'Current version is {version}')
    chosen = sui.input('Option', str)
    options = {
        '1': servermenu().menu,
        '2': tokenmenu().menu,
        '3': spammingmenu().menu,
        '4': bypassmenu().menu,
        '5': vcmenu().menu,
        '6': webhookmenu().menu,
        '7': adminmenu().menu,
        '8': proxymenu().menu,
        '9': massdmmenu().menu,
        '10': massreportmenu().menu,
        '11': lambda: sui.paidnotif(),
        '12': lambda: sui.paidnotif(),
        '13': lambda: sui.paidnotif(),
        '14': lambda: sui.paidnotif(),
        '15': lambda: sui.paidnotif(),
        '19': suppliers.menu,
        '20': lambda: exit(),
    }

    if chosen in options:
        try:
            options[chosen]()
            
        except Exception as error:
            logger.error('Failed to run', error)

    else:
        logger.log('Invalid option')

    logger.log('Enter to continue')
    input('')