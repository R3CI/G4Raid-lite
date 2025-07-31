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
        [sys.executable, '-m', 'pip', 'install', '--force-reinstall', pkg],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
