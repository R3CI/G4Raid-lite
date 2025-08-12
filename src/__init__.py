# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged


import sys, os
os.system('cls')
os.system('title G4Spam FREE - launching...')
import time
import copy
import uuid
import httpx
import json
import socket
import base64
import string
import random
from tkinter import Tk, filedialog, messagebox
from curl_cffi import exceptions as cfex
import ctypes
import re
import traceback
import threading as threadinglib
import webbrowser
import curl_cffi as curlcffi_
from pypresence import Presence
from curl_cffi import requests as curlcffi
from datetime import datetime as dt, timedelta, timezone
from tkinter import Tk
from tkinter import ttk, Frame
from urllib.parse import quote
from tkinter.filedialog import askopenfilename, askdirectory
import os
import base64
import random
import string
import json
from typing import List, Dict, Optional, Tuple, Union, NamedTuple
from collections import defaultdict, namedtuple

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