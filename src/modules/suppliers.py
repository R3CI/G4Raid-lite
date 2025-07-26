# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.ui import ui

class suppliers:
    def menu():
        module = 'Suppliers'
        sui = ui(module)
        sui.prep()
        sui.createmenu([
            'G4Spam PAID',
            'Lime SOURCE'
            'Private raiders',
            'Proxies',
            'Tokens',
            'Back'
        ])
        chosen = sui.input('Option', str)

        if chosen == '1': 
            webbrowser.open('https://g4tools.top')

        elif chosen == '2':
            webbrowser.open('https://r3ci.sell.app')

        elif chosen == '3':
            sui.log('DM me on discord')
            input('')

        elif chosen == '4':
            sui.createmenu([
                'Best recommended',
                'Second best',
                'Back'
            ])
            chosen = sui.input('Option', str)

            if chosen == '1':   webbrowser.open('https://www.tokenu.net?ref=r3ci')
            elif chosen == '2': webbrowser.open('https://www.vital-proxies.com/?ref=m3dm062i')
            else:               suppliers.menu()

        elif chosen == '5':
            sui.createmenu([
                #'My shop (UHQ + AGE GARAUNTEED)',
                'Best overall recommended',
                'Second best (Deal with caution)',
                'Back'
            ])
            chosen = sui.input('Option', str)

            if chosen == '1':   webbrowser.open('https://www.tokenu.net?ref=r3ci')
            elif chosen == '2': webbrowser.open('https://lzt.market/discord/')
            else:               suppliers.menu()

        elif chosen == '6':
            sui.createmenu([
                'Soon'
            ])

        elif chosen == '7':
            return

        else:
            suppliers.menu()