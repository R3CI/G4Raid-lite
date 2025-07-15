@echo off
cls
setlocal EnableDelayedExpansion

REM ==========================================
REM CONFIGURATION - Change this value to control installation mode
REM ==========================================
REM Set ENVIRONMENT_MODE to:
REM   1 = Virtual Environment Mode (SAFE) - Isolates dependencies from system Python
REM   2 = Simple Mode - Installs packages directly to your system
REM ==========================================
set "ENVIRONMENT_MODE=1"
REM ==========================================

echo [*] Discord Support: https://discord.gg/spamming
echo [*] Issues ^& Updates: https://github.com/r3ci/g4spam
echo.

start https://discord.gg/spamming
start https://t.me/g4spam
start https://g4tools.top

call :check_required_files
if !errorlevel! neq 0 exit /b 1

call :check_python_installation
if !errorlevel! neq 0 exit /b 1

call :check_pip_installation
if !errorlevel! neq 0 exit /b 1

call :set_environment_mode
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
    echo [!] main.py not found - script might be zipped or incomplete
    echo     Please unzip the archive before running
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

if not exist "src\" (
    echo [!] src folder not found - script might be zipped or incomplete
    echo     Please unzip the archive before running
    echo     Make sure to download the FULL zip from GitHub, not just main.py
    echo     To download the full zip: click Code ^(green button^) then Download ZIP
    echo     Need help? Join our Discord: https://discord.gg/spamming
    pause
    exit /b 1
)

if not exist "requirements.txt" (
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

:set_environment_mode
echo [*] Environment Mode Configuration:
echo.

if "!ENVIRONMENT_MODE!"=="1" (
    set "USE_VENV=true"
    echo [+] Virtual Environment Mode (SAFE) - Selected
    echo     - Isolates dependencies from system Python
    echo     - Safer and cleaner installation
) else if "!ENVIRONMENT_MODE!"=="2" (
    set "USE_VENV=false"
    echo [+] Simple Mode - Selected
    echo     - Installs packages directly to your system
    echo     - Quick and simple but may cause conflicts
) else (
    echo [!] Invalid ENVIRONMENT_MODE value: !ENVIRONMENT_MODE!
    echo     Valid values are 1 (Virtual Environment) or 2 (Simple Mode)
    echo     Defaulting to Virtual Environment Mode
    set "USE_VENV=true"
    set "ENVIRONMENT_MODE=1"
)

echo.
echo [*] To change mode, edit ENVIRONMENT_MODE variable at the top of this script
echo     Current mode: !ENVIRONMENT_MODE!
echo.
exit /b 0

:setup_environment
if "!USE_VENV!"=="true" (
    call :setup_virtual_environment
    if !errorlevel! equ 0 (
        echo [+] Virtual environment setup successful
        exit /b 0
    ) else (
        echo [!] Virtual environment setup failed
        echo.
        set /p "fallback=Would you like to try simple mode instead? (y/n) [y]: "
        if "!fallback!"=="" set "fallback=y"
        if /i "!fallback!"=="y" (
            set "USE_VENV=false"
            echo [*] Switching to simple mode
        ) else (
            echo [!] Setup cancelled by user
            pause
            exit /b 1
        )
    )
)

if "!USE_VENV!"=="false" (
    echo [*] Using simple mode
    echo [!] WARNING: Dependencies will be installed globally
)

echo [+] Environment setup complete
exit /b 0

:setup_virtual_environment
echo [*] Setting up virtual environment...

python -m venv --help >nul 2>&1
if !errorlevel! neq 0 (
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
        echo [!] Failed to activate virtual environment
        exit /b 1
    )
) else (
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

:install_dependencies
if "!USE_VENV!"=="true" (
    echo [*] Installing dependencies in virtual environment...
    echo [*] Upgrading pip to latest version...
    python -m pip install --upgrade pip --quiet --disable-pip-version-check >nul 2>&1
    if !errorlevel! neq 0 (
        echo [!] Failed to upgrade pip ^(trying without quiet mode^)
        python -m pip install --upgrade pip --disable-pip-version-check
        if !errorlevel! neq 0 (
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
            echo [!] Critical dependency installation failure
            echo     Need help? Join our Discord: https://discord.gg/spamming
            pause
            exit /b 1
        )
    )
) else (
    echo [*] Installing dependencies in simple mode...
    pip install -r requirements.txt
    if !errorlevel! neq 0 (
        echo [!] Failed to install dependencies
        echo     Need help? Join our Discord: https://discord.gg/spamming
        pause
        exit /b 1
    )
)

echo [+] All dependencies installed successfully
exit /b 0

:run_application
echo.
echo [*] Starting application...
echo ==========================================

if "!USE_VENV!"=="true" (
    python main.py
) else (
    py main.py
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
    echo [+] Application finished ^(simple mode^)
)
echo.
echo [*] Thanks for using our application!
echo [*] Discord Support: https://discord.gg/spamming
echo [*] Star us on GitHub: https://github.com/r3ci/g4spam
echo.
echo Press any key to exit...
pause >nul
exit /b 0