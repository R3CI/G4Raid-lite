# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.files import files
from src.util.rpc import RPC

class ui:
    def __init__(self, module=None):
        self.module = module

    def gettimestamp(self):
        timestamp = dt.now().strftime('%H:%M:%S')
        return timestamp

    def log(self, text, ts=False):
        if ts:
            ts = f'{co.main}[{co.reset}{self.gettimestamp()}{co.main}] '
        else:
            ts = ''
        print(f'{ts}{co.main}[{co.reset}{self.module}{co.main}] {co.main}[{co.reset}{text}{co.main}]{co.reset}')

    def title(self, title):
        os.system(f'title {title}')

    def cls(self):
        os.system('cls')

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

    def bar(self):
        bar = fr'{co.main}«{len(files.gettokens())}» Tokens                   «{len(files.getproxies())}» Proxies'

        bar = self.center(text=bar, size=os.get_terminal_size().columns)
        bar = str(bar)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def banner(self):
        banner = fr'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = self.center(banner, os.get_terminal_size().columns)

        print(banner)
        
    def menu(self):
        menu = fr'''{co.reset}
«THIS IS THE ONLY REAL GITHUB https:/github.com/R3CI/G4Spam OTHERS ARE MALWRE»
«USING FREE VERSION MEANING LESS UPDATES AND WORSE BYPASSING»
«GET PAID VERSION ON https://g4tools.top»

«01» Server menu        «06» Funny menu         «11» Token filler       «16» Admin menu  
«02» Token menu         «07» Exploit menu       «12» Invite checker     «17» Proxy menu  
«03» Spamming menu      «08» Mass report menu   «13» None               «18» Webhook menu
«04» Bypass menu        «09» None               «14» None               «19» Suppliers   
«05» VC menu            «10» None               «15» Scraping menu      «20» Exit        
'''     
        menu: str = self.center(text=menu, size=os.get_terminal_size().columns)
        
        for char in ['»', '«']:
            menu = menu.replace(char, f'{co.main}{char}{co.reset}')

        print(menu)

    def input(self, text, expected=str):
        module = f'{co.main}[{co.reset}{self.module}{co.main}] ' if self.module else ''
        
        if expected == bool:
            while True:
                result = input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}({co.reset}y/n{co.main}) {co.main}» {co.reset}')
                if result.lower() in ['y', 'yes', 'true']:
                    return True
                
                elif result.lower() in ['n', 'no', 'false']:
                    return False
                
                else:
                    self.log(f'Invalid input expected y/n got {result} - please type y for yes or n for no')
        
        while True:
            result = input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}» {co.reset}')

            if expected == str:
                return result
            
            try:
                return expected(result)
            
            except Exception as e:
                if expected == int:
                    self.log(f'Invalid input expected number - please enter a whole number like 1, 5, 100')

                elif expected == float:
                    self.log(f'Invalid input expected decimal - please enter a number like 1.5, 3.14, 10.0')

                else:
                    self.log(f'Invalid input expected {str(expected)}')

    def delayinput(self):
        if self.module == None:
            module = ''
        else:
            module = f'{co.main}[{co.reset}{self.module}{co.main}] '

        x = input(f'{module}{co.main}[{co.reset}Delay{co.main}] {co.main}» {co.reset}')
        try:
            float(x)
        except:
            return 0
        
        return x

    def createmenu(self, options):
        toprint = []
        for i, option in enumerate(options, 1):
            number = str(i).zfill(2)
            toprint.append(f'{co.main}[{co.reset}{number}{co.main}] » {co.main}[{co.reset}{option}{co.main}]')
        
        print('\n'.join(toprint))

    def optionmenu(self, options):
        self.prep()
        self.createmenu(list(options.keys()) + ['Back'])

    def prep(self):
        RPC.update(f'Using {self.module}')
        self.cls()
        self.banner()
        if self.module != None:
            self.title(f'G4Spam FREE - {self.module} - github.com/R3CI/G4Spam - discord.gg/spamming - Made by r3ci')

    def cut(self, text, length, end=''):
        try:
            text = str(text)
            length = int(length)
            if len(text) <= length:
                return text
            return text[:length] + end
        
        except Exception:
            return str(text)


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
            webbrowser.open('https://g4tools.top')
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
