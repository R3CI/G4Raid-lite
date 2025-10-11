import os
import re
import webbrowser
from src import *
from src.utils.printing import printer

class console:
    def __init__(self, module='Console'):
        self.module = module

    def cls(self):
        os.system('clear')

    def clear_title(self):
        pass

    def title(self, title):
        pass

    def center(self, text, size=None):
        if size is None:
            try:
                size = os.get_terminal_size().columns
            except:
                size = 80
                
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
        bar = f'{co.main}«{tokens}» Tokens                   «{proxies}» Proxies'

        bar = self.center(text=bar)
        bar = str(bar)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def printbanner(self):
        banner = f'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\\__ \\/ __ \\/ __ `/ __ `__ \\
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\\____/  /_/ /____/ .___/\\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = self.center(banner)

        print(banner)

    def printmenu(self, page=1):
        page1 = f'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«01» Server Joiner       «06» Channel Spammer      «11» Checker             «16» NickName Changer
«02» Server Leaver       «07» MultiChannel Spamemr «12» Bio Changer         «17» Invite Checker  
«03» Server Checker      «08» Reply spammer        «13» Avatar Changer      «18» Invite info     
«04» Channel Checker     «09» None                 «14» ClanTag Changer     «19» Tutorials       
«05» Anti Ban            «10» None                 «15» Displayname Changer «20» Next page       
'''     
        page1 = self.center(text=page1)
        
        for char in ['»', '«']:
            page1 = page1.replace(char, f'{co.main}{char}{co.reset}')

        page2 = f'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«21» Reaction Bypass     «26» Restorecord Bypass   «31» Chat Crasher        «36» Profile Reporter
«22» Button Bypass       «27» AuthGG Bypass        «32» AuditLog Fucker     «37» Message Reporter
«23» Button Menu Bypass  «28» None                 «33» Reaction Speller    «38» Token Filler    
«24» Rule Bypass         «29» None                 «34» None                «39» Prev page       
«25» Onboarding Bypass   «30» None                 «35» None                «40» Next page       
'''     
        page2 = self.center(text=page2)
        
        for char in ['»', '«']:
            page2 = page2.replace(char, f'{co.main}{char}{co.reset}')

        page3 = f'''{co.reset}
«https://g4tools.top»
«FREE VERSION WITH LIMITED FEATURES BUY FULL ON https://g4tools.top»

«41» Mass Send           «46» None                 «51» None                «56» ID Scraper      
«42» Mass Call           «47» None                 «52» None                «57» Username Scraper
«43» Mass Friend         «48» None                 «53» None                «58» None            
«44» None                «49» None                 «54» None                «59» None            
«45» None                «50» None                 «55» None                «60» Prev page       
'''     
        page3 = self.center(text=page3)
        
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
            try:
                result = input(prompt).strip()
            except (KeyboardInterrupt, EOFError):
                print()
                exit()
        
            if not result:
                if expected == str:
                    return result
                else:
                    printer.info('Input required please enter a value')
                    continue

            if expected == bool:
                if result.lower() in ['y', 'yes', 'true', '1']:
                    return True
                
                elif result.lower() in ['n', 'no', 'false', '0']:
                    return False
                
                else:
                    printer.info('Invalid input please enter y/yes/true or n/no/false')
                    continue
            
            if expected == str:
                return result
            
            try:
                converted = expected(result)
                return converted
                
            except ValueError:
                if expected == int:
                    printer.info('Please enter a whole number (eg 1 42 100)')
                elif expected == float:
                    printer.info('Please enter a decimal number (eg 1.5 3.14 10.0)')
                else:
                    printer.info(f'Invalid format expected {expected.__name__}')
                continue

    def prep(self):
        self.cls()
        self.printbanner()

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

    def runchooser(self):
        printer.info('This is a PAID ONLY feature.', 'Premium')
        printer.info('Visit https://g4tools.top to get the full version', 'Premium')
        input('Press enter to continue...')