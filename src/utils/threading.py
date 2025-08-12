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