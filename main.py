import os
os.system('clear')

from src import *
from src.utils.rpc import RPC
from src.utils.console import console
from src.utils.files import files; files.check()
from src.utils.config import get
from src.utils.printing import printer
console = console('Main')

page = 1
while True:
    console.clear_title()
    console.cls()
    console.printbanner()
    console.printbar(0, 0)
    console.printmenu(page)
    printer.info('Get FULL on https://g4tools.top')
    printer.info('G4Spam FREE made by r3ci <3')

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
    input('Press enter to continue...')