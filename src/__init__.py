# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

version = '1.0.6'

import sys, os;sys.dont_write_bytecode = True;os.environ['PYTHONDONTWRITEBYTECODE'] = '1';os.system('cls');os.system('title G4Spam FREE - launching...')
import subprocess
import time

if sys.prefix == sys.base_prefix:
    print('[!] Not inside virtual environment Launching run.bat in 3s')
    time.sleep(3)
    script = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'run.bat')
    os.system(f'start "" "{script}"')
    sys.exit()

from importlib.metadata import version as getpackageversion
from datetime import datetime as dt, timezone
from pypresence import Presence
import webbrowser
import re
import json
import traceback
import copy
import threading as threadinglib
import uuid
import requests
import string
import curl_cffi as curlcffi_
import random
import base64
from curl_cffi import requests as curlcffi
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import zipfile
import shutil
import tempfile
from pathlib import Path

webbrowser.open('https://github.com/R3CI/G4Spam')
webbrowser.open('https://discord.gg/spamming')
webbrowser.open('https://t.me/g4spam')
webbrowser.open('https://g4tools.top')

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

class co:
    main = rgb(80, 5, 255)
    red = rgb(255, 0, 0)
    darkred = rgb(139, 0, 0)
    green = rgb(0, 255, 0)
    blue = rgb(0, 0, 255)
    yellow = rgb(255, 255, 0)
    orange = rgb(255, 165, 0)
    pink = rgb(255, 105, 180)
    cyan = rgb(0, 255, 255)
    magenta = rgb(255, 0, 255)
    lime = rgb(191, 255, 0)
    teal = rgb(0, 128, 128)
    indigo = rgb(75, 0, 130)
    violet = rgb(238, 130, 238)
    brown = rgb(139, 69, 19)
    grey = rgb(128, 128, 128)
    black = rgb(0, 0, 0)
    white = rgb(255, 255, 255)
    reset = '\033[0m'

from src.util.errorhandler import handle_exception
sys.excepthook = handle_exception
