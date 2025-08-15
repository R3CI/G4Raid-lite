# This free version of G4Spam has been discontinued.
# To use the full version, buy it for 10 USD here: https://g4tools.top
# This script will show a notice and open the purchase page automatically.

import tkinter as tk, webbrowser, os

os.system('cls')

root = tk.Tk()
root.overrideredirect(True)
root.geometry('400x180+{}+{}'.format(root.winfo_screenwidth()//2-200, root.winfo_screenheight()//2-90))
root.configure(bg='black')
root.attributes('-topmost', True)
root.attributes('-alpha', 0)

tk.Label(root, text='Notice', bg='black', fg='white', font=('Segoe UI', 10, 'bold')).pack(anchor='w', padx=10, pady=5)
tk.Label(root, text='The free version has been discontinued', bg='black', fg='white', font=('Segoe UI', 11)).pack(pady=5)
tk.Label(root, text='Buy the FULL premium version for only 10 USD\nhttps://g4tools.top', bg='black', fg='white', font=('Segoe UI', 10)).pack(pady=5)
tk.Button(root, text='Close', command=root.destroy, bg='white', fg='black').pack(pady=10)

root.after(2500, lambda: webbrowser.open('https://g4tools.top'))
root.after(2500, lambda: webbrowser.open('https://discord.gg/spamming'))

def fade(a=0):
    if a < 1:
        root.attributes('-alpha', a)
        root.after(20, lambda: fade(a+0.05))
fade()

root.mainloop()
