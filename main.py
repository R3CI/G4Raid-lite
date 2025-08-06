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

    logger.log(f'G4Spam FREE has been launched over {launches} times, with {stars} stars on github! Thank you!')
    logger.log(f'Get FULL version on https://g4tools.top')
    time.sleep(1)

    webbrowser.open('https://discord.gg/spamming')
    webbrowser.open('https://t.me/g4tool')
    webbrowser.open('https://g4tools.top')
    
    chosen = sui.input('Option', int)
    options = {
        1:  lambda: servermenu().menu(),
        2:  lambda: tokenmenu().menu(),
        3:  lambda: spammingmenu().menu(),
        4:  lambda: bypassmenu().menu(),
        5:  lambda: vcmenu().menu(),
        6:  lambda: funnymenu().menu(),
        7:  lambda: exploitmenu().menu(),
        8:  lambda: massreportmenu().menu(),
        9:  lambda: logger.log('This is a placeholder'),
        10: lambda: logger.log('This is a placeholder'),
        11: lambda: sui.paidnotif(),
        12: lambda: sui.paidnotif(),
        13: lambda: logger.log('This is a placeholder'),
        14: lambda: logger.log('This is a placeholder'),
        15: lambda: scrapingmenu().menu(),
        16: lambda: adminmenu().menu(),
        17: lambda: proxymenu().menu(),
        18: lambda: webhookmenu().menu(),
        19: lambda: suppliers.menu(),
        20: lambda: sys.exit(0),
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