import sys
import webbrowser
import os
import re
import time

webbrowser.open('https://g4tools.top')
webbrowser.open('https://discord.gg/spamming')
webbrowser.open('https://r3ci.dev')

flag = False
try:
    from pypresence import Presence
except:
    os.system('pip install pypresence')
    flag = True

try:
    from datetime import datetime as dt
except:
    os.system('pip install datetime')
    flag = True

if flag:
    input('Please restart the script')
    exit()

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

class co:
    main = rgb(80, 5, 255)
    red = rgb(255, 69, 0)
    darkred = rgb(87, 2, 2)
    green = rgb(12, 250, 0)
    blue = rgb(30, 144, 255)
    yellow = rgb(255, 215, 0)
    orange = rgb(255, 140, 0)
    deeporange = rgb(201, 105, 6)
    pink = rgb(255, 105, 180)
    cyan = rgb(0, 255, 255)
    magenta = rgb(255, 0, 255)
    lime = rgb(12, 250, 0)
    indigo = rgb(138, 43, 226)
    grey = rgb(169, 169, 169)
    black = rgb(69, 69, 69)
    white = rgb(255, 255, 255)

    success = lime
    error = red
    locked = darkred
    debug = grey
    warning = yellow
    ratelimit = orange
    cloudflare = deeporange
    solver = indigo
    captcha = cyan
    
    reset = '\033[0m'

from src.utils.files import files
files.check()