# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

import sys
sys.dont_write_bytecode = True
import os
import re
import subprocess

os.system('cls')
print('[*] Discord Support: https://discord.gg/spamming')
print('[*] Github Repo: https://github.com/r3ci/g4spam')
print()
v = sys.version_info
if v.major != 3 or v.minor < 11 or (v.major == 3 and v.minor == 12 and v.micro == 10):
    print('[!] Bad Python version detected:', sys.version.split()[0])
    print('[!] Install Python 3.12.7 and make sure to add it to PATH')
    input('The software might NOT work properly, PRESS ENTER TO INGORE AND CONTINUE')

try:
    subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
except:
    print('[!] pip not found or broken')
    print('[!] Reinstall Python 3.12.7 with pip and Add to PATH')
    input('The software might NOT work properly, PRESS ENTER TO INGORE AND CONTINUE')
os.system('cls')

try:
    import time
    from datetime import datetime as dt, timezone
    from pypresence import Presence
    import webbrowser
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
    import zipfile
    import tempfile
    from curl_cffi import requests as curlcffi
    from tkinter import Tk, Frame
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename, askdirectory
    import shutil
    from pathlib import Path
    
except Exception as e:
    print('Installing modules...')
    print('Please wait it can take some time')
    print('You can ignore the 2 line error messages')
    
    modules = [
        'pypresence', 
        'requests', 
        'curl-cffi', 
        'pathlib2',
        'datetime',
        'tkinter',
        'tkinter',
        'webbrowser',
        'zipfile',
        'tempfile'
    ]
    
    for module in modules:
        subprocess.run(['py', '-m', 'pip', 'install', '--force-reinstall', module], capture_output=True)
        subprocess.run(['python', '-m', 'pip', 'install', '--force-reinstall', module], capture_output=True)
        print(f'Installed {module}')
    
    missing = re.search(r"No module named ['\"]([^'\"]+)['\"]", str(e))
    if missing:
        subprocess.run(['py', '-m', 'pip', 'install', '--force-reinstall', missing.group(1)], capture_output=True)
        subprocess.run(['python', '-m', 'pip', 'install', '--force-reinstall', missing.group(1)], capture_output=True)
        print(f'Installed {missing.group(1)}')
    
    print('Done Restart script')
    input('Press Enter...')
    sys.exit()

print('Making sure curl_cffi is up to date...')
os.system('py -m pip install -U curl_cffi')
os.system('python -m pip install -U curl_cffi')
os.system('cls')
os.system('title G4Spam FREE - launching...')

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
