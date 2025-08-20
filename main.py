# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

import os
os.system('cls')

os.system('title G4Spam FREE - launching...')
from src import *
from src.utils.rpc import RPC
from src.utils.console import console
from src.utils.files import files; files.check(); files.guardtokens()
from src.utils.config import get
from src.utils.printing import printer
console = console('Main')

if get.proxies.enabled():
    printer.info(f'PRXOIES are PAID ONLY! get paid on https://g4tools.top/g4spam if you want to use them', 'Config')
    printer.info(f'Enter to continue', 'Config')
    input('')

if get.solver.enabled():
    printer.info(f'SOLVER SUPPORT is PAID ONLY! get paid on https://g4tools.top/g4spam if you want to use it', 'Config')
    printer.info(f'Enter to continue', 'Config')
    input('')

page = 1
while True:
    console.title('G4Spam - g4tools.top - discord.gg/spamming - Made by r3ci')
    console.cls()
    console.printbanner()
    console.printbar(len(files.gettokens()), len(files.getproxies()))
    console.printmenu(page)
    printer.info(f'Get FULL on https://g4tools.top')
    printer.info(f'G4Spam FREE made by r3ci <3')

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

    else:
        console.runchooser()
    
    printer.info('Finished running option', 'Main')
    input('')
