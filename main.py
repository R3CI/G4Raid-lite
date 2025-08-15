import os
import webbrowser
import time
import ctypes

os.system('cls')

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)

print('The free version has been discontinued')
print('Buy the FULL premium version for only 10 USD on https://g4tools.top')
time.sleep(2.5)
webbrowser.open('https://g4tools.top')
webbrowser.open('https://discord.gg/spamming')
input('')
