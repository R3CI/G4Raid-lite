@echo off
cls
setlocal EnableDelayedExpansion

set "USE_VENV=true"

echo ==========================================
echo Python Application Setup Script
echo ==========================================
echo.
echo [*] Discord Support: https://discord.gg/spamming
echo [*] Issues ^& Updates: https://github.com/r3ci/g4spam
echo.

call :check_required_files
if !errorlevel! neq 0 exit /b 1

call :check_python_installation
if !errorlevel! neq 0 exit /b 1

call :check_pip_installation
if !errorlevel! neq 0 exit /b 1

call :setup_environment
if !errorlevel! neq 0 exit /b 1

call :install_dependencies
if !errorlevel! neq 0 exit /b 1

call :run_application
goto :end

:check_required_files
echo [*] Checking required files...

if not exist "main.py" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] main.py not found - script might be zipped or incomplete
    echo     Please unzip the archive before running
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

if not exist "src\" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] src folder not found - script might be zipped or incomplete
    echo     Please unzip the archive before running
    echo     Make sure to download the FULL zip from GitHub, not just main.py
    echo     To download the full zip: click Code ^(green button^) then Download ZIP
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] requirements.txt not found
    echo     This file is required to install dependencies
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

echo [+] All required files found
exit /b 0

:check_python_installation
echo [*] Checking Python installation...

python --version >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] Python is not installed or not in PATH
    call :show_python_install_guide
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [+] Python !PYTHON_VERSION! detected
exit /b 0

:check_pip_installation
echo [*] Checking pip installation...

pip --version >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] pip is not installed or not in PATH
    echo.
    echo To fix pip issues:
    echo   1. Try: python -m ensurepip --upgrade
    echo   2. If that fails, reinstall Python with "Add Python to PATH" checked
    echo   3. Or download get-pip.py from https://bootstrap.pypa.io/get-pip.py
    echo   4. Then run: python get-pip.py
    echo.
    echo Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

echo [+] pip is available
exit /b 0

:setup_environment
echo [*] Setting up Python environment...

if "!USE_VENV!"=="true" (
    call :setup_virtual_environment
    if !errorlevel! equ 0 (
        echo [+] Virtual environment setup successful
        exit /b 0
    ) else (
        echo [!] Virtual environment setup failed, using compatibility mode
        echo.
        set "USE_VENV=false"
    )
)

echo [*] Using compatibility mode
call :setup_fake_venv
echo [+] Environment setup complete
exit /b 0

:setup_virtual_environment
echo [*] Checking virtual environment support...

python -m venv --help >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] venv module not available
    echo     Trying to install virtualenv...
    pip install virtualenv --quiet --disable-pip-version-check >nul 2>&1
    if !errorlevel! neq 0 (
        echo [!] Failed to install virtualenv module
        exit /b 1
    )
)

if not exist "venv\" (
    echo [*] Creating virtual environment...
    python -m venv venv
    if !errorlevel! neq 0 (
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Failed to create virtual environment
        echo     This might be due to:
        echo       - Insufficient permissions
        echo       - Antivirus blocking
        echo       - Corrupted Python installation
        echo       - Insufficient disk space
        exit /b 1
    )
    echo [+] Virtual environment created successfully
) else (
    echo [+] Virtual environment already exists
)

echo [*] Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call "venv\Scripts\activate.bat"
    if !errorlevel! neq 0 (
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Failed to activate virtual environment
        exit /b 1
    )
) else (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] Virtual environment activation script not found
    echo     Try deleting venv folder and running script again
    exit /b 1
)

echo [*] Verifying virtual environment activation...
python -c "import sys; print('[+] Using Python:', sys.executable)" 2>nul
if !errorlevel! neq 0 (
    echo [!] Virtual environment verification failed
    exit /b 1
)

exit /b 0

:setup_fake_venv
echo [*] Setting up compatibility environment...

if not exist "fake_venv\" (
    mkdir "fake_venv"
    mkdir "fake_venv\Scripts"
    mkdir "fake_venv\Lib"
    mkdir "fake_venv\Lib\site-packages"
)

for /f "tokens=*" %%i in ('python -c "import sys; print(sys.executable)"') do set PYTHON_EXE=%%i
for /f "tokens=*" %%i in ('python -c "import sys; print(sys.prefix)"') do set PYTHON_PREFIX=%%i

echo @echo off > "fake_venv\Scripts\activate.bat"
echo set "VIRTUAL_ENV=%cd%\fake_venv" >> "fake_venv\Scripts\activate.bat"
echo set "PATH=%cd%\fake_venv\Scripts;%%PATH%%" >> "fake_venv\Scripts\activate.bat"
echo set "_OLD_VIRTUAL_PROMPT=%%PROMPT%%" >> "fake_venv\Scripts\activate.bat"
echo set "PROMPT=(fake_venv) %%PROMPT%%" >> "fake_venv\Scripts\activate.bat"

echo import sys > "fake_venv\pyvenv.cfg"
echo home = %PYTHON_PREFIX% >> "fake_venv\pyvenv.cfg"
echo include-system-site-packages = true >> "fake_venv\pyvenv.cfg"
echo version = 3.0.0 >> "fake_venv\pyvenv.cfg"

:: This is used to fake venv if the normal launch failed this is not malwre or anything ask chat gpt if u dont trust or something
python -c "import sys; import os; sys.path.insert(0, os.path.join(os.getcwd(), 'fake_venv')); import site; site.addsitedir(os.path.join(os.getcwd(), 'fake_venv', 'Lib', 'site-packages')); import builtins; builtins.base_prefix = sys.prefix; sys.prefix = os.path.join(os.getcwd(), 'fake_venv'); sys.exec_prefix = sys.prefix; exec(open('fake_venv\\fake_sys.py', 'w').write('import sys\nsys.prefix = \\'%s\\'\nsys.base_prefix = \\'%s\\'\nsys.exec_prefix = \\'%s\\'\n' % (sys.prefix, builtins.base_prefix, sys.exec_prefix)) or '')"

call "fake_venv\Scripts\activate.bat"
exit /b 0

:install_dependencies
if "!USE_VENV!"=="true" (
    echo [*] Installing dependencies in virtual environment...
) else (
    echo [*] Installing dependencies in compatibility mode...
)

echo [*] Upgrading pip to latest version...
python -m pip install --upgrade pip --quiet --disable-pip-version-check >nul 2>&1
if !errorlevel! neq 0 (
    echo [!] Failed to upgrade pip ^(trying without quiet mode^)
    python -m pip install --upgrade pip --disable-pip-version-check
    if !errorlevel! neq 0 (
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Critical pip upgrade failure
        echo     Need help? Join our Discord: https://discord.gg/spamming
        pause
        exit /b 1
    )
)

echo [*] Installing/updating all dependencies...
pip install --upgrade -r requirements.txt --quiet --disable-pip-version-check >nul 2>&1
if !errorlevel! neq 0 (
    echo [!] Failed to install/update requirements ^(showing detailed output^)
    echo.
    pip install --upgrade -r requirements.txt --disable-pip-version-check
    if !errorlevel! neq 0 (
        echo.
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Critical dependency installation failure
        echo     Common solutions:
        echo       - Check internet connection
        echo       - Run as administrator
        echo       - Disable antivirus temporarily
        echo       - Check requirements.txt for invalid packages
        echo       - Try: pip install --upgrade -r requirements.txt --no-cache-dir
        echo.
        echo     Need help? Join our Discord: https://discord.gg/spamming
        pause
        exit /b 1
    )
)

echo [+] All dependencies installed/updated successfully
exit /b 0

:run_application
echo.
echo [*] Starting application...
echo ==========================================

if "!USE_VENV!"=="false" (
    :: This is used to fake venv if the normal launch failed this is not malwre or anything ask chat gpt if u dont trust or something
    python -c "import sys; import os; sys.path.insert(0, os.path.join(os.getcwd(), 'fake_venv')); import importlib.util; spec = importlib.util.spec_from_file_location('fake_sys', os.path.join(os.getcwd(), 'fake_venv', 'fake_sys.py')); fake_sys = importlib.util.module_from_spec(spec); spec.loader.exec_module(fake_sys); sys.modules['fake_sys'] = fake_sys; exec(open('main.py').read())" 2>nul
    if !errorlevel! neq 0 (
        python -c "import sys; import os; old_prefix = sys.prefix; sys.prefix = os.path.join(os.getcwd(), 'fake_venv'); sys.base_prefix = old_prefix; exec(open('main.py').read())"
        if !errorlevel! neq 0 (
            echo.
            echo [!] Application failed to start in compatibility mode
            echo     Trying direct execution...
            python main.py
        )
    )
) else (
    python main.py
)

if !errorlevel! neq 0 (
    echo.
    echo [!] Application exited with error code !errorlevel!
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b !errorlevel!
)
exit /b 0

:show_python_install_guide
echo.
echo Step-by-step Python installation:
echo   1. Go to https://www.python.org/downloads/
echo   2. Click "Download Python" ^(latest version^)
echo   3. Run the downloaded installer
echo   4. CRITICAL: Check "Add Python to PATH" checkbox
echo   5. Click "Install Now"
echo   6. Wait for installation to complete
echo   7. Restart your computer ^(recommended^)
echo   8. Run this script again
echo.
echo Need help? Join our Discord: https://discord.gg/spamming
exit /b 0

:end
endlocal
echo.
if "!USE_VENV!"=="true" (
    echo [+] Application finished ^(virtual environment active^)
) else (
    echo [+] Application finished ^(compatibility mode^)
)
echo.
echo [*] Thanks for using G4Spam!
echo [*] Discord Server https://discord.gg/spamming
echo [*] Star us on GitHub https://github.com/r3ci/g4spam
echo.
echo Press any key to exit...
pause >nul
exit /b 0