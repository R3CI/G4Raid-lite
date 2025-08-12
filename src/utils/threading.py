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

class handledthread(threadinglib.Thread):
    def run(self):
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)

        except Exception as e:
            logger.error(f'Failed to run thread » {e}')

class threading:
    def __init__(self, func, tokens=[], args=[], delay=0):
        self.func = func
        self.tokens = tokens
        self.args = args
        self.delay = delay
        self.threads: list[threadinglib.Thread] = []
        self.work()

    def work(self):
        try:
            if not self.tokens:
                logger.warning(f'No tokens have been passed please input them into the file')
                return

            for token in self.tokens:
                t = handledthread(target=self.func, args=(token, *self.args))
                self.threads.append(t)
                t.start()

                if self.delay > 0:
                    time.sleep(self.delay)

            for thread in self.threads:
                thread.join()

        except KeyboardInterrupt:
            pass