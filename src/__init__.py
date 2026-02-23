import sys, os
os.system('cls')
os.system('title G4Raid-lite - launching...')
import subprocess
try:
    import time
    import traceback
    import re
    import webbrowser
    import random
    from pypresence import Presence
    from datetime import datetime as dt, timedelta, timezone
    from urllib.parse import urlparse, quote
    from collections import defaultdict, namedtuple
    from tkinter.filedialog import askopenfilename, askdirectory
    import json
    from tkinter.filedialog import askopenfilename, askdirectory
    from tkinter import ttk, Frame, Tk, filedialog, messagebox
except Exception as e:
    print(e)
    packages = [
        'datetime',
        'pypresence',
    ]

    for pg in packages:
        os.system('python -m pip install --upgrade ' + pg)

    input('Run the script again')

webbrowser.open('https://g4tools.cc', autoraise=False)
webbrowser.open('https://t.me/g4toolscc', autoraise=False)
webbrowser.open('https://discord.gg/spamming', autoraise=True)

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

    infolog = pink
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

from src.utils.errorhandler import errorhandler
sys.excepthook = errorhandler

from src.utils.files import files
files.check()
