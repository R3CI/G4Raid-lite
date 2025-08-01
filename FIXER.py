import sys
import subprocess

packages = [
    'pypresence', 
    'requests', 
    'curl-cffi', 
    'pathlib2',
    'datetime',
    'tkinter',
    'tkinter',
    'webbrowser',
    'zipfile',
    'tempfile'
]
for pkg in packages:
    subprocess.run(
        ['python', '-m', 'pip', 'install', '--force-reinstall', pkg]
    )


input('If there ware any issues they shuld be fixed now')