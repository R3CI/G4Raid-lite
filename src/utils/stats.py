# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged


from src import *
from src.utils.logging import logger
import shutil

class stats:
    SUCCEDED = 'succeeded'
    CAPTCHA = 'captcha'
    FAILED = 'failed'
    REASONS = 'reasons'

    def __init__(self, name, categories=None):
        self.categories = categories or [self.SUCCEDED, self.CAPTCHA, self.FAILED]
        if self.REASONS not in self.categories:
            self.categories.append(self.REASONS)

        self.data = {}
        self.path = f'data\\stats\\{name}'
        self._lock = threadinglib.Lock()
        for category in self.categories:
            self.data[category] = []

        self.reset()
        shutil.rmtree(self.path, ignore_errors=True)
        os.makedirs(self.path, exist_ok=True)
   
    def reset(self):
        with self._lock:
            for category in self.categories:
                self.data[category] = []
                filepath = f'{self.path}\\{category}.txt'
                if os.path.exists(filepath):
                    os.remove(filepath)
   
    def getdatetime(self):
        return dt.now().strftime('%Y-%m-%d %H:%M:%S')
   
    def append(self, category, token, error=None):
        with self._lock:
            if category not in self.categories:
                self.categories.append(category)
                self.data[category] = []
            if self.REASONS not in self.categories:
                self.categories.append(self.REASONS)
                self.data[self.REASONS] = []
            
            self.data[category].append(token)
            if error:
                self.data[self.REASONS].append(f'{token} » {error}')
            
            self.savecategorytofile(category)
            
            if error:
                self.savecategorytofile(self.REASONS)
    
    def savecategorytofile(self, category):
        filepath = os.path.join(self.path, f'{category}.txt')
        tempfilepath = filepath + '.tmp'
        try:
            with open(tempfilepath, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.data[category]))
            if os.path.exists(filepath):
                os.remove(filepath)
            os.rename(tempfilepath, filepath)
            
        except Exception as e:
            logger.error(f'Failed to save stats for {category} » {e}')
            if os.path.exists(tempfilepath):
                os.remove(tempfilepath)