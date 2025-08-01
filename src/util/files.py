# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
logger = logger('Files')

_files = [
    'data\\tokens.txt',
    'data\\proxies.txt'
]
_dirs = [
    'data'
]

class files:
    def gettokens():
        with open('data\\tokens.txt', 'r') as f:
            tokens = f.read().splitlines()
        return tokens

    def getproxies():
        with open('data\\proxies.txt', 'r') as f:
            return f.read().splitlines()

    def runtasks():
        for d in _dirs:
            if not os.path.exists(d):
                try:
                    os.mkdir(d)
                    
                except Exception as e:
                    logger.error(f'Failed to create directory {d}, try to run as admin and move the file to desktop (REMEMBER TO UNZIP)', e)
                    input('')
        
        for f in _files:
            if not os.path.exists(f):
                try:
                    with open(f, 'w') as f:
                        f.write('')
                        
                except Exception as e:
                    logger.error(f'Failed to create file {f}, try to run as admin and move the file to desktop (REMEMBER TO UNZIP)', e)
                    input('')

    def choosefile():
        root = Tk()
        root.withdraw()
        return askopenfilename()

    def choosefolder():
        root = Tk()
        root.withdraw()
        return askdirectory()
