from src import *
from src.utils.config import get

def choicehandler():
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
        webbrowser.open('https://g4tools.cc')
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

    ttk.Label(inner, text='Lite version is no longer mentained. As of now only the paid one is mentained (15$ lifetime)', anchor='center', justify='center').pack(padx=20, pady=(20, 15))

    btns = Frame(inner, bg='#1e1e1e')
    btns.pack(pady=(0, 20))

    ttk.Button(btns, text='No i do not want the best tool on the market', command=onok).pack(side='left', padx=5)
    ttk.Button(btns, text='Buy paid', command=ongetpaid).pack(side='left', padx=5)

    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)
    root.geometry(f'+{x}+{y}')
    webbrowser.open('https://g4tools.cc')
    fadein(root)
    root.mainloop()

class printing:
    def timestamp():
        return dt.now().strftime('%H:%M:%S ')

    def info(text, text2=None):
        if text2:
            first = f'{co.main}[{co.reset}{text2}{co.main}] {co.reset}»{co.reset} '
        else:
            first = ''

        log = f'{co.main}[{co.reset}{text}{co.main}]{co.reset}'

        for char in ['»', '«']:
            log = log.replace(char, f'{co.main}{char}{co.reset}')

        log = f'{first}{log}'
            
        print(log)
