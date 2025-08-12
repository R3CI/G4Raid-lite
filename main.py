import os
os.system('cls')
os.system('title G4Spam FREE - launching...')
from src import *
from src.utils.rpc import RPC
from src.utils.console import console
from src.utils.files import files; files.check(); files.guardtokens()
from src.utils.config import get
from src.utils.logging import logger
from src.funcs import *
console = console('Main')

time.sleep(0.5)
console.cls()
console.title('G4Spam - g4tools.top - discord.gg/spamming - Made by r3ci')
console.printbanner()

if get.debug.enabled():
    logger.info('Debug mode enabled', 'Config')

logger.info('Connecting accounts is PAID only!', 'Onliner')

time.sleep(1)

if get.proxies.enabled():
    logger.info(f'PRXOIES are PAID ONLY! get paid on https://g4tools.top/g4spam if you want to use them', 'Config')
    logger.info(f'Enter to continue', 'Config')
    input('')

if get.solver.enabled():
    logger.info(f'SOLVER SUPPORT is PAID ONLY! get paid on https://g4tools.top/g4spam if you want to use it', 'Config')
    logger.info(f'Enter to continue', 'Config')
    input('')

page = 1
while True:
    console.title('G4Spam - g4tools.top - discord.gg/spamming - Made by r3ci')
    console.cls()
    console.printbanner()
    console.printbar(len(files.gettokens()), len(files.getproxies()))
    console.printmenu(page)
    logger.info(f'Get full on https://g4tools.top')
    logger.info(f'G4Spam FREE made by r3ci <3')

    choice = console.input('Option', int)

    if choice == 20:
        page += 1
        continue

    elif choice == 39:
        page -= 1
        continue

    elif choice == 40:
        page += 1
        continue

    elif choice == 60:
        page -= 1
        continue

    options = {
        1: joiner().menu,
        2: leaver().menu,
        3: serverchecker().menu,
        4: channelchecker().menu,
        5: console.paidnotif(),
        6: channelspammer().menu,
        7: console.paidnotif(),
        8: console.paidnotif(),
        9: lambda: logger.info('This is a placeholder', 'Menu'),
        10: lambda: logger.info('This is a placeholder', 'Menu'),
        11: checker().menu,
        12: console.paidnotif(),
        13: console.paidnotif(),
        14: console.paidnotif(),
        15: console.paidnotif(),
        16: console.paidnotif(),
        17: invitechecker().menu,
        18: inviteinfo().menu,
        19: lambda: logger.info('Not implemented yet', 'Menu'),
        #NEXT PAGE
        21: reactionbypass().menu,
        22: console.paidnotif(),
        23: lambda: logger.info('Not implemented yet', 'Menu'),
        24: console.paidnotif(),
        25: console.paidnotif(),
        26: console.paidnotif(),
        27: console.paidnotif(),
        28: lambda: logger.info('This is a placeholder', 'Menu'),
        29: lambda: logger.info('This is a placeholder', 'Menu'),
        30: lambda: logger.info('This is a placeholder', 'Menu'),
        31: console.paidnotif(),
        32: lambda: logger.info('Not implemented yet', 'Menu'),
        33: console.paidnotif(),
        34: lambda: logger.info('This is a placeholder', 'Menu'),
        35: lambda: logger.info('This is a placeholder', 'Menu'),
        36: console.paidnotif(),
        37: console.paidnotif(),
        38: console.paidnotif(),
        #PREV PAGE
        #NEXT PAGE
        41: console.paidnotif(),
        42: lambda: logger.info('Not implemented yet', 'Menu'),
        43: console.paidnotif(),
        44: lambda: logger.info('This is a placeholder', 'Menu'),
        45: lambda: logger.info('This is a placeholder', 'Menu'),
        46: lambda: logger.info('This is a placeholder', 'Menu'),
        47: lambda: logger.info('This is a placeholder', 'Menu'),
        48: lambda: logger.info('This is a placeholder', 'Menu'),
        49: lambda: logger.info('This is a placeholder', 'Menu'),
        50: lambda: logger.info('This is a placeholder', 'Menu'),
        51: lambda: logger.info('This is a placeholder', 'Menu'),
        52: lambda: logger.info('This is a placeholder', 'Menu'),
        53: lambda: logger.info('This is a placeholder', 'Menu'),
        54: lambda: logger.info('This is a placeholder', 'Menu'),
        55: lambda: logger.info('This is a placeholder', 'Menu'),
        56: lambda: logger.info('Not implemented yet', 'Menu'),
        57: lambda: logger.info('Not implemented yet', 'Menu'),
        58: lambda: logger.info('This is a placeholder', 'Menu'),
        59: lambda: logger.info('This is a placeholder', 'Menu'),
        #PREV PAGE

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