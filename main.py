import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; os.system('cls')
from src import *

from src.util.ui import ui
from src.util.logger import Logger
from src.util.other import other

logger = Logger()
logger.log(text='Getting repo stars...', ts=True)
stars = other.getrepostars()

logger.log(text='Finished booting G4Spam', ts=True)

while True:
    ui.title(f'G4Spam - github.com/R3CI/G4Spam ({stars}) - discord.gg/spamming - Made by r3ci')
    ui.cls()
    ui.banner()
    ui.bar()
    ui.menu()

    logger.log(text='Welcome to G4Spam made by r3ci <3 github.com/R3CI/G4Spam', ts=False)
    chosen = ui.input(text='Option')

    options = {
        '20': lambda: exit(),
        '0': lambda: ui.createmenu(['cipek', 'cipek2', 'cipek3'])
    }
    try:
        options[chosen]()
    except KeyError:
        logger.error(text='Invalid option', ts=False)
    
    logger.log(text='Finished, enter to continue')
    input('')