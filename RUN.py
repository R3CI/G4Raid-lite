# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

import os
import sys
import subprocess
import webbrowser

def checkpython():
    v = sys.version_info
    if v.major != 3 or v.minor < 11 or (v.major == 3 and v.minor == 12 and v.micro == 10):
        print('[!] Bad Python version detected:', sys.version.split()[0])
        print('[!] Install Python 3.12.7 and make sure to add it to PATH')
        input('The software might NOT work properly, PRESS ENTER TO INGORE AND CONTINUE')

def checkpip():
    try:
        subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except:
        print('[!] pip not found or broken')
        print('[!] Reinstall Python 3.12.7 with pip and Add to PATH')
        input('The software might NOT work properly, PRESS ENTER TO INGORE AND CONTINUE')

os.system('cls')

checkpython()
checkpip()

print('[*] Discord Support: https://discord.gg/spamming')
print('[*] Github Repo: https://github.com/r3ci/g4spam')
print()

webbrowser.open('https://discord.gg/spamming')
webbrowser.open('https://t.me/g4tool')
webbrowser.open('https://g4tools.top')

os.system('python main.py')

input('Press Enter to continue...')
