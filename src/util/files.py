from src import *

_files = [
    'data\\tokens.txt',
    'data\\proxies.txt'
]
_dirs = [
    'data'
]

class files:
    @staticmethod
    def write(path: str, text: str, method: str):
        with open(path, method) as f:
            f.write(text)

    @staticmethod
    def read(path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    @staticmethod
    def createdir(path: str):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def createfile(path: str):
        if not os.path.exists(path):
            open(path, 'w').close()

    @staticmethod
    def removefile(path: str):
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def joinpath(*args) -> str:
        return os.path.join(*args)

    @staticmethod
    def getsize(path: str) -> int:
        return os.path.getsize(path)

    @staticmethod
    def isfile(path: str) -> bool:
        return os.path.isfile(path)

    @staticmethod
    def isdir(path: str) -> bool:
        return os.path.isdir(path)

    @staticmethod
    def exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def walk(path: str) -> tuple:
        return os.walk(path)

    @staticmethod
    def listdir(path: str) -> list:
        return os.listdir(path)

    @staticmethod
    def getcwd() -> str:
        return os.getcwd()

    @staticmethod
    def runtasks():
        for d in _dirs:
            if not files.exists(d):
                files.createdir(d)
        
        for f in _files:
            if not files.exists(f):
                files.createfile(f)

files.runtasks()