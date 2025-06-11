# i will leave this code here cuz i fr dont know what does it do lol :P

version = 1.0
import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; os.system('cls')
import subprocess
import time
try:
    from datetime import datetime as dt
    import os
    import webbrowser
    import re
    import requests
except ModuleNotFoundError:
    print('Installing requirements in 5s')
    time.sleep(5)
    os.system('pip install -r requirements.txt')
    print('Rebooting the script in 5s')
    time.sleep(5)
    subprocess.Popen(f'start cmd /k python "{os.path.abspath(__file__)}"', shell=True)
    sys.exit()

#webbrowser.open('https://discord.gg/spamming')
#webbrowser.open('https://t.me/g4spam')

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

class co:
    main = rgb(80, 5, 255)
    gmain = [80, 5, 255]
    gmain_ = [120, 50, 255]

    red = rgb(255, 0, 0)
    gred = [255, 100, 100]
    gred_ = [180, 0, 0]

    green = rgb(0, 255, 0)
    ggreen = [100, 255, 100]
    ggreen_ = [0, 180, 0]

    blue = rgb(0, 0, 255)
    gblue = [100, 100, 255]
    gblue_ = [0, 0, 180]

    yellow = rgb(255, 255, 0)
    gyellow = [255, 255, 150]
    gyellow_ = [200, 200, 0]

    orange = rgb(255, 165, 0)
    gorange = [255, 190, 100]
    gorange_ = [200, 100, 0]

    pink = rgb(255, 105, 180)
    gpink = [255, 155, 200]
    gpink_ = [200, 80, 150]

    cyan = rgb(0, 255, 255)
    gcyan = [100, 255, 255]
    gcyan_ = [0, 180, 180]

    magenta = rgb(255, 0, 255)
    gmagenta = [255, 100, 255]
    gmagenta_ = [180, 0, 180]

    lime = rgb(191, 255, 0)
    glime = [220, 255, 100]
    glime_ = [150, 200, 0]

    teal = rgb(0, 128, 128)
    gteal = [80, 180, 180]
    gteal_ = [0, 100, 100]

    indigo = rgb(75, 0, 130)
    gindigo = [120, 60, 160]
    gindigo_ = [50, 0, 90]

    violet = rgb(238, 130, 238)
    gviolet = [250, 180, 250]
    gviolet_ = [200, 100, 200]

    brown = rgb(139, 69, 19)
    gbrown = [180, 120, 70]
    gbrown_ = [100, 50, 10]

    grey = rgb(128, 128, 128)
    ggrey = [180, 180, 180]
    ggrey_ = [90, 90, 90]

    black = rgb(0, 0, 0)
    gblack = [50, 50, 50]
    gblack_ = [0, 0, 0]

    white = rgb(255, 255, 255)
    gwhite = [240, 240, 240]
    gwhite_ = [200, 200, 200]

    reset = '\033[0m'