# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Raid-lite

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

from src import *
from src.utils.rpc import RPC
from src.utils.console import console
from src.utils.files import files; files.check()
from src.utils.config import get
from src.utils.logging import logger
from src.funcs import *
console = console('Main')

time.sleep(0.5)
console.cls()
console.title('G4Raid - g4tools.cc - discord.gg/spamming - Made by r3ci')
console.printbanner()

if get.debug.enabled():
    logger.info('Debug mode enabled', 'Config')
while True:
    console.title('G4Raid-lite - g4tools.cc - discord.gg/spamming - Made by r3ci')
    console.cls()
    console.printbanner()
    console.printbar(len(files.gettokens()), 0)
    console.printmenu()
    logger.info(f'G4Raid-lite made by r3ci <3')

    choice = console.input('Option', str)

    options = {
        'SU': suppliers().menu,
        'su': suppliers().menu,
        'SC': lambda: logger.paidonly(),
        'sc': lambda: logger.paidonly(),
        '1': lambda: logger.paidonly(),
        '2': leaver().menu,
        '3': serverchecker().menu,
        '4': channelchecker().menu,
        '5': lambda: logger.info('Will unpatch this soon', 'Menu'),
        '6': channelspammer().menu,
        '7': lambda: logger.paidonly(),
        '8': lambda: logger.paidonly(),
        '9': lambda: logger.paidonly(),
        '10': lambda: logger.paidonly(),
        '11': checker().menu,
        '12': biochanger().menu,
        '13': lambda: logger.paidonly(),
        '14': lambda: logger.paidonly(),
        '15': displaynamechanger().menu,
        '16': nicknamechanger().menu,
        '17': lambda: logger.paidonly(),
        '18': lambda: logger.paidonly(),
        '19': lambda: logger.info('Not implemented yet', 'Menu'),
        '20': verifybypasses().menu,
    }
     
    if choice in options:
        try:
            options[choice]()
            
        except Exception as e:
            logger.error(f'Failed to run {str(choice)} » {str(e)}')
    else:
        logger.error(f'Invalid option » {str(choice)}')

    logger.info('Finished running option', 'Main')
    input('')