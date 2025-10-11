import os
from src import *
from src.utils.printing import printer

class files:
    @staticmethod
    def check():
        filestomake = [
            'data',
            'data/scrapes',
            'data/tokenchecker',
            'data/stats'
        ]

        folderstomake = [
            'data/tokens.txt',
            'data/proxies.txt'
        ]

        for path in filestomake:
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
            except PermissionError as e:
                printer.error(f'Permission denied creating directories: {e}')
                input('')
            except Exception as e:
                printer.error(f'Error creating directories: {e}')
                input('')
        
        for path in folderstomake:
            try:
                if not os.path.exists(path):
                    with open(path, 'w') as f:
                        f.write('')
            except PermissionError as e:
                printer.error(f'Permission denied creating files: {e}')
                input('')
            except Exception as e:
                printer.error(f'Error creating files: {e}')
                input('')

    @staticmethod
    def choosefile():
        printer.info('File selection not available in Termux', 'System')
        path = input('Enter file path manually: ')
        return path

    @staticmethod
    def choosefolder():
        printer.info('Folder selection not available in Termux', 'System')
        path = input('Enter folder path manually: ')
        return path

    @staticmethod
    def gettokens():
        try:
            with open('data/tokens.txt', 'r') as f:
                tokens = [line.strip() for line in f if line.strip()]
            return tokens
        except:
            return []

    @staticmethod
    def getproxies():
        try:
            with open('data/proxies.txt', 'r') as f:
                proxies = [line.strip() for line in f if line.strip()]
            return proxies
        except:
            return []