from src import *
from src.utils.logging import logger

Token = namedtuple('Token', ['email', 'password', 'token'])

class files:
    @staticmethod
    def check():
        filestomake = [
            'data',
            'data\\scrapes',
            'data\\tokenchecker',
            'data\\stats'
        ]

        folderstomake = [
            'data\\tokens.txt',
            'data\\proxies.txt'
        ]

        for path in filestomake:
            try:
                if not os.path.exists(path):
                    os.makedirs(path)

            except PermissionError as e:
                logger.error(f'Permission denied creating files/directories, please move G4Raid-lite to a different place desktop/own folder best » {e}')
                input('')

            except Exception as e:
                logger.error(f'Error creating files » {e}')
                input('')
        
        for path in folderstomake:
            try:
                if not os.path.exists(path):
                    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                        f.write('')
    
            except PermissionError as e:
                logger.error(f'Permission denied creating files/directories, please move G4Raid-lite to a different place desktop/own folder best » {e}')
                input('')

            except Exception as e:
                logger.error(f'Error creating files » {e}')
                input('')

    @staticmethod
    def gettokens():
        tokens = []

        try:
            with open('data\\tokens.txt', 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.read().splitlines()
                for line in lines:
                    if not line.strip():
                        continue

                    coloncount = line.count(':')
                    if coloncount == 1 or coloncount > 2:
                        logger.error(f'Invalid token format the correct format is EMAIL:PASSWORD:TOKEN if this IS your format keep the token only as ur supplier is a idiot » {line}')

                    parts = line.split(':', 2)
                    if len(parts) == 3:
                        email, password, token = parts
                    else:
                        email = None
                        password = None
                        token = parts[0]
                    
                    token = Token(email, password, token)
                    tokens.append(token)
                    random.shuffle(tokens)
        
        except PermissionError as e:
            logger.error(f'Permission denied reading files/directories, please move G4Raid to a different place desktop/own folder best » {e}')
            input('')

        except Exception as e:
            logger.error(f'Error reading files » {e}')
            input('')

        return tokens
    
    def choosefile():
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        path = filedialog.askopenfilename(
            title='Select a file',
            filetypes=[
                ('All files', '*.*'),
            ]
        )
        root.destroy()
        return path

    def choosefolder():
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        path = filedialog.askdirectory(title='Select a folder')
        root.destroy()
        return path

