# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

# This code is not the best as i honestly dont care much about it its made to work well and i do not need it to be good code overall as i dont update this often
# Only the paid version will get updates often this is a side thing nothing crazy
# Remember this is literary the only up to date FREE tool out on github all the other ones are old or skids from 2023
# If you wana get more features with the cost of flgging ur stuff do but you will make ur tokens flagged

from src import *
from src.utils.printing import printer

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
                printer.error(f'Permission denied creating files/directories, please move g4spam to a different place desktop/own folder best » {e}')
                input('')

            except Exception as e:
                printer.error(f'Error creating files » {e}')
                input('')
        
        for path in folderstomake:
            try:
                if not os.path.exists(path):
                    with open(path, 'w') as f:
                        f.write('')
    
            except PermissionError as e:
                printer.error(f'Permission denied creating files/directories, please move g4spam to a different place desktop/own folder best » {e}')
                input('')

            except Exception as e:
                printer.error(f'Error creating files » {e}')
                input('')

    @staticmethod
    def gettokens() -> List[Token]:
        tokens = []

        try:
            with open('data\\tokens.txt', 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                for line in lines:
                    if not line.strip():
                        continue

                    colon_count = line.count(':')
                    if colon_count == 1 or colon_count > 2:
                        printer.error(f'Invalid token format the correct format is EMAIL:PASSWORD:TOKEN if this IS your format keep the token only as ur supplier is a idiot » {line}')

                    parts = line.split(':', 2)
                    if len(parts) == 3:
                        email, password, token = parts
                    else:
                        email = None
                        password = None
                        token = parts[0]
                    
                    token = Token(email, password, token)
                    tokens.append(token)
        
        except PermissionError as e:
            printer.error(f'Permission denied reading files/directories, please move g4spam to a different place desktop/own folder best » {e}')
            input('')

        except Exception as e:
            printer.error(f'Error reading files » {e}')
            input('')

        return tokens
        
    def getproxies():
        proxies = []
        try:
            with open('data/proxies.txt', 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                for line in lines:
                    try:
                        if '@' in line:
                            proxies.append(line)

                        else:
                            printer.error(f'Invalid proxy format the correct format is user:password@host:port » {line}')

                    except:
                        continue
                   
        except PermissionError as e:
            printer.error(f'Permission denied reading files/directories, please move g4spam to a different place desktop/own folder best » {e}')
            input('')
            
        except Exception as e:
            printer.error(f'Error reading files » {e}')
            input('')
               
        return proxies

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


    def guardtokens():
        def blik_runner_cwel():
            if not os.path.exists('data\\tokens.txt'):
                os._exit(1)
            mtime = os.path.getmtime('data\\tokens.txt')

            while True:
                time.sleep(1)
                if os.path.getmtime('data\\tokens.txt') != mtime:
                    root = Tk()
                    root.withdraw()
                    root.attributes('-topmost', True)
                    messagebox.showwarning('Tokens File Motidifed', 'The tokens file was modified restart the software to make sure everything works fine', parent=root)
                    root.destroy()
                    os._exit(0)
        
        threadinglib.Thread(target=blik_runner_cwel).start()

