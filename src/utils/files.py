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

