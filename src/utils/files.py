from src import *

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
            if not os.path.exists(path):
                os.makedirs(path)
        
        for path in folderstomake:
            if not os.path.exists(path):
                with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                    f.write('')

    @staticmethod
    def gettokens():
        tokens = []
        with open('data\\tokens.txt', 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.read().splitlines()
            for line in lines:
                if not line.strip():
                    continue

                coloncount = line.count(':')
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

