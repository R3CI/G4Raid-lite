# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

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