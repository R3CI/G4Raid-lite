# This free version of G4Spam has been discontinued.
# To use the full version, buy it for 10 USD here: https://g4tools.top
# This script will show a notice and open the purchase page automatically.

import tkinter as tk, webbrowser, os

os.system('cls')

os.system('title G4Spam FREE - launching...')
from src import *
from src.utils.rpc import RPC
from src.utils.console import console
from src.utils.files import files; files.check(); files.guardtokens()
from src.utils.config import get
from src.utils.logging import logger
console = console('Main')

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
    logger.info(f'Get FULL on https://g4tools.top')
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
        1 : lambda: console.paidnotif(),
        2 : lambda: console.paidnotif(),
        3 : lambda: console.paidnotif(),
        4 : lambda: console.paidnotif(),
        5 : lambda: console.paidnotif(),
        6 : lambda: console.paidnotif(),
        7 : lambda: console.paidnotif(),
        8 : lambda: console.paidnotif(),
        9 : lambda: console.paidnotif(),
        10: lambda: console.paidnotif(),
        11: lambda: console.paidnotif(),
        12: lambda: console.paidnotif(),
        13: lambda: console.paidnotif(),
        14: lambda: console.paidnotif(),
        15: lambda: console.paidnotif(),
        16: lambda: console.paidnotif(),
        17: lambda: console.paidnotif(),
        18: lambda: console.paidnotif(),
        19: lambda: console.paidnotif(),
        #NEXT PAGE
        21: lambda: console.paidnotif(),
        22: lambda: console.paidnotif(),
        23: lambda: console.paidnotif(),
        24: lambda: console.paidnotif(),
        25: lambda: console.paidnotif(),
        26: lambda: console.paidnotif(),
        27: lambda: console.paidnotif(),
        28: lambda: console.paidnotif(),
        29: lambda: console.paidnotif(),
        30: lambda: console.paidnotif(),
        31: lambda: console.paidnotif(),
        32: lambda: console.paidnotif(),
        33: lambda: console.paidnotif(),
        34: lambda: console.paidnotif(),
        35: lambda: console.paidnotif(),
        36: lambda: console.paidnotif(),
        37: lambda: console.paidnotif(),
        38: lambda: console.paidnotif(),
        #PREV PAGE
        #NEXT PAGE
        41: lambda: console.paidnotif(),
        42: lambda: console.paidnotif(),
        43: lambda: console.paidnotif(),
        44: lambda: console.paidnotif(),
        45: lambda: console.paidnotif(),
        46: lambda: console.paidnotif(),
        47: lambda: console.paidnotif(),
        48: lambda: console.paidnotif(),
        49: lambda: console.paidnotif(),
        50: lambda: console.paidnotif(),
        51: lambda: console.paidnotif(),
        52: lambda: console.paidnotif(),
        53: lambda: console.paidnotif(),
        54: lambda: console.paidnotif(),
        55: lambda: console.paidnotif(),
        56: lambda: console.paidnotif(),
        57: lambda: console.paidnotif(),
        58: lambda: console.paidnotif(),
        59: lambda: console.paidnotif(),
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