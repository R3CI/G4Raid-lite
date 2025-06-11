from src import *
from datetime import datetime as dt

class Logger:
    def __init__(self, module: str = 'Logger'):
        self.module = module

    def get_timestamp(self) -> str:
        return dt.now().strftime('%H:%M:%S')

    def log(self, text: str, ts: bool = False):
        timestamp = f'{co.main}[{co.reset}{self.get_timestamp()}{co.main}] ' if ts else ''
        print(f'{timestamp}{co.main}[{co.reset}{self.module}{co.main}] {co.main}[{co.reset}{text}{co.main}]{co.reset}')

    def error(self, text: str, error: str = '', ts: bool = False):
        endstr = f'{co.grey}({co.grey}{error}{co.grey}){co.reset}' if error else ''
        timestamp = f'{co.main}[{co.reset}{self.get_timestamp()}{co.main}] ' if ts else ''
        print(f'{timestamp}{co.main}[{co.reset}{self.module}{co.main}] {co.main}[{co.red}{text}{co.main}] {endstr}{co.reset}')