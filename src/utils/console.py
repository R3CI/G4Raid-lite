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

class console:
    def __init__(self, module='Console'):
        self.module = module

    def cls(self):
        os.system('cls')

    def title(self, title):
        os.system(f'title {title}')

    def center(self, text, size):
        text = str(text)
        lines = text.split('\n')
        centeredlines = []
        for line in lines:
            visibleline = re.sub(r'\033\[[0-9;]*m', '', line)
            visiblelength = len(visibleline)
            
            if visiblelength >= size:
                centeredlines.append(line)
            else:
                padding = (size - visiblelength) // 2
                centeredlines.append(' ' * padding + line)
        
        return '\n'.join(centeredlines)

    def printbar(self, tokens, proxies):
        bar = fr'{co.main}«{tokens}» Tokens                   «{proxies}» Proxies'

        bar = self.center(text=bar, size=os.get_terminal_size().columns)
        bar = str(bar)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def printbanner(self):
        banner = fr'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = self.center(banner, os.get_terminal_size().columns)

        print(banner)

    def printmenu(self, page=1):
        page1 = fr'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«01» Server Joiner       «06» Channel Spammer      «11» Checker             «16» NickName Changer
«02» Server Leaver       «07» MultiChannel Spamemr «12» Bio Changer         «17» Invite Checker  
«03» Server Checker      «08» Reply spammer        «13» Avatar Changer      «18» Invite info     
«04» Channel Checker     «09» None                 «14» ClanTag Changer     «19» Tutorials       
«05» Anti Ban            «10» None                 «15» Displayname Changer «20» Next page       
'''     
        page1: str = self.center(text=page1, size=os.get_terminal_size().columns)
        
        for char in ['»', '«']:
            page1 = page1.replace(char, f'{co.main}{char}{co.reset}')



        page2 = fr'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«21» Reaction Bypass     «26» Restorecord Bypass   «31» Chat Crasher        «36» Profile Reporter
«22» Button Bypass       «27» AuthGG Bypass        «32» AuditLog Fucker     «37» Message Reporter
«23» Button Menu Bypass  «28» None                 «33» Reaction Speller    «38» Token Filler    
«24» Rule Bypass         «29» None                 «34» None                «39» Prev page       
«25» Onboarding Bypass   «30» None                 «35» None                «40» Next page       
'''     
        page2: str = self.center(text=page2, size=os.get_terminal_size().columns)
        
        for char in ['»', '«']:
            page2 = page2.replace(char, f'{co.main}{char}{co.reset}')

        page3 = fr'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«41» Mass Send           «46» None                 «51» None                «56» ID Scraper      
«42» Mass Call           «47» None                 «52» None                «57» Username Scraper
«43» Mass Friend         «48» None                 «53» None                «58» None            
«44» None                «49» None                 «54» None                «59» None            
«45» None                «50» None                 «55» None                «60» Prev page       
'''     
        page3: str = self.center(text=page3, size=os.get_terminal_size().columns)
        
        for char in ['»', '«']:
            page3 = page3.replace(char, f'{co.main}{char}{co.reset}')


        if page == 1:
            print(page1) 

        elif page == 2:
            print(page2)

        elif page == 3:
            print(page3)

    def input(self, text, expected=str):
        module = f'{co.main}[{co.reset}{self.module}{co.main}] ' if self.module else ''
        
        promptparts = [f'{co.main}[{co.reset}{text}{co.main}]']
        
        if expected == bool:
            promptparts.append(f'{co.main}({co.reset}{co.lime}y{co.reset}/{co.red}n{co.reset}{co.main})')
        
        prompt = ' '.join(promptparts) + f' {co.reset}» {co.reset}'
        
        while True:
            result = input(prompt).strip()
        
            if not result:
                if expected == str:
                    return result
                else:
                    logger.info('Input required please enter a value')
                    continue

            if expected == bool:
                if result.lower() in ['y', 'yes', 'true', '1']:
                    return True
                
                elif result.lower() in ['n', 'no', 'false', '0']:
                    return False
                
                else:
                    logger.info('Invalid input please enter y/yes/true or n/no/false')
                    continue
            
            if expected == str:
                return result
            
            try:
                converted = expected(result)
                return converted
                
            except ValueError:
                if expected == int:
                    logger.info('Please enter a whole number (eg 1 42 100)')

                elif expected == float:
                    logger.info('Please enter a decimal number (eg 1.5 3.14 10.0)')

                else:
                    logger.info(f'Invalid format expected {expected.__name__}')
                continue

    def prep(self):
        self.cls()
        self.printbanner()
        if self.module != None:
            self.title(f'G4Spam FREE - {self.module} - g4tools.top - discord.gg/spamming - Made by r3ci')

    def createmenu(self, options):
        toprint = []
        for i, option in enumerate(options, 1):
            number = str(i).zfill(2)
            toprint.append(f'{co.main}[{co.reset}{number}{co.main}] » {co.main}[{co.reset}{option}{co.main}]')
        
        print('\n'.join(toprint))

    def printcustommenu(self, options):
        options = dict(options)
        self.prep()
        self.createmenu(list(options.keys()) + ['Back'])

    def paidnotif(self):
        def fadein(win, alpha=0):
            alpha = round(alpha + 0.05, 2)
            if alpha <= 1:
                win.attributes('-alpha', alpha)
                win.after(10, fadein, win, alpha)

        def close(win, alpha=1):
            alpha = round(alpha - 0.05, 2)
            if alpha > 0:
                win.attributes('-alpha', alpha)
                win.after(10, close, win, alpha)
            else:
                win.destroy()

        def onok():
            close(root)

        def ongetpaid():
            webbrowser.open('https://g4tools.top/g4spam')
            close(root)

        root = Tk()
        root.title('')
        root.overrideredirect(True)
        root.attributes('-topmost', True)
        root.attributes('-alpha', 0)
        root.configure(bg='#000000')

        outer = Frame(root, bg='#000000')
        outer.pack(padx=2, pady=2)

        inner = Frame(outer, bg='#1e1e1e')
        inner.pack()

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#1e1e1e', foreground='#ffffff', font=('Segoe UI', 11))
        style.configure('TButton', font=('Segoe UI', 10), foreground='#ffffff', background='#2d2d30', borderwidth=0, padding=6)
        style.map('TButton',
            background=[('active', '#3e3e42')],
            relief=[('pressed', 'sunken'), ('!pressed', 'raised')]
        )

        ttk.Label(inner, text='This is a PAID ONLY feature.', anchor='center', justify='center').pack(padx=20, pady=(20, 15))

        btns = Frame(inner, bg='#1e1e1e')
        btns.pack(pady=(0, 20))

        ttk.Button(btns, text='OK', command=onok).pack(side='left', padx=5)
        ttk.Button(btns, text='Get Paid Now', command=ongetpaid).pack(side='left', padx=5)

        root.update_idletasks()
        w = root.winfo_width()
        h = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (w // 2)
        y = (root.winfo_screenheight() // 2) - (h // 2)
        root.geometry(f'+{x}+{y}')

        fadein(root)
        root.mainloop()