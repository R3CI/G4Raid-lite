from src import *
from src.util.files import files

class ui:
    def title(title: str):
        os.system(f'title {title}')

    def cls():
        os.system('cls')

    def center(text: str, size: int) -> str:
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
    
    def bar():
        tokens = len(files.read('data\\tokens.txt'))
        proxies = len(files.read('data\\proxies.txt'))
        bar = f"{co.main}«{tokens}» Tokens{' ' * 20}«{proxies}» Proxies"

        bar: str = ui.center(text=bar, size=os.get_terminal_size().columns)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def banner():
        banner = fr'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = ui.center(banner, os.get_terminal_size().columns)

        print(banner)
        
    def menu():
        menu = f'''{co.main}
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                │
│   «01» Server managment   «06» Webhook menu       «11» Annoying menu      «18» Unk             │
│   «02» Token managment    «07» Nuking menu        «12» Unk                «17» Unk             │
│   «03» Spamming           «08» Proxy menu         «13» Unk                «18» Unk             │
│   «04» Bypass menu        «09» Mass DM menu       «14» Unk                «19» Unk             │
│   «05» VC menu            «10» Mass report menu   «15» Unk                «20» Exit            │
│                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
'''     
        menu: str = ui.center(text=menu, size=os.get_terminal_size().columns)
        
        for char in ['╭', '╯', '╮', '╰', '─', '│', '»', '«']:
            menu = menu.replace(char, f'{co.main}{char}{co.reset}')

        print(menu)

    def input(text: str, module: str = None, yesno: bool = False) -> str | bool:
        module_str = f'{co.main}[{co.reset}{module}{co.main}] ' if module else ''
        prompt = f'{module_str}{co.main}[{co.reset}{text}{co.main}]'
        if yesno:
            result = input(f'{prompt} {co.main}({co.reset}y/n{co.main}) {co.reset}')
            return result.lower() in ('y', 'yes')
        return input(f'{prompt} {co.main}» {co.reset}')

    def createmenu(options: list):
        print('\n'.join(
            f'{co.main}[{co.reset}{str(i+1).zfill(2)}{co.main}] » {co.main}[{co.reset}{option}{co.main}]'
            for i, option in enumerate(options)
        ))
