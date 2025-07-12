@echo off
cls
setlocal EnableDelayedExpansion

if not exist "main.py" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] main.py not found - script might be zipped or incomplete
    echo Please unzip the archive before running
    pause
    exit /b 1
)

if not exist "src\" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] src folder not found - script might be zipped or incomplete
    echo Please unzip the archive before running
    echo Make sure to download the FULL zip from GitHub, not just main.py
    echo To download the full zip: click Code ^(green button^) then Download ZIP
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] requirements.txt not found
    echo This file is required to install dependencies
    pause
    exit /b 1
)

echo [*] Checking Python installation...
python --version >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] Python is not installed or not in PATH
    echo.
    echo Step-by-step Python installation:
    echo 1. Go to https://www.python.org/downloads/
    echo 2. Click "Download Python 3.12.x" ^(latest version^)
    echo 3. Run the downloaded installer
    echo 4. IMPORTANT: Check "Add Python to PATH" during installation
    echo 5. Click "Install Now"
    echo 6. Restart this script after installation
    pause
    exit /b 1
)

echo [*] Checking pip installation...
pip --version >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] pip is not installed or not in PATH
    echo.
    echo To fix pip issues:
    echo 1. Try: python -m ensurepip --upgrade
    echo 2. If that fails, reinstall Python with "Add Python to PATH" checked
    echo 3. Or download get-pip.py from https://bootstrap.pypa.io/get-pip.py
    echo 4. Then run: python get-pip.py
    pause
    exit /b 1
)

echo [+] pip is available

echo [*] Checking virtual environment support...
python -m venv --help >nul 2>&1
if !errorlevel! neq 0 (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] venv module not available
    echo Try installing: pip install virtualenv
    pause
    exit /b 1
)

echo [*] Checking virtual environment...
if not exist "venv\" (
    echo [*] Creating virtual environment...
    python -m venv venv
    if !errorlevel! neq 0 (
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Failed to create virtual environment
        echo This might be due to:
        echo - Insufficient permissions
        echo - Antivirus blocking
        echo - Corrupted Python installation
        pause
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
        pause
        exit /b 1
    )
) else (
    echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
    echo [!] Virtual environment activation script not found
    echo Try deleting venv folder and running script again
    pause
    exit /b 1
)

echo [*] Verifying virtual environment activation...
python -c "import sys; print('[+] Using Python:', sys.executable)"

echo [*] Upgrading pip to latest version...
python -m pip install --upgrade pip --quiet --disable-pip-version-check
if !errorlevel! neq 0 (
    echo [!] Failed to upgrade pip
    echo Trying without quiet mode...
    python -m pip install --upgrade pip --disable-pip-version-check
    if !errorlevel! neq 0 (
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Critical pip upgrade failure
        pause
        exit /b 1
    )
)

echo [*] Installing/updating all dependencies...
pip install --upgrade -r requirements.txt --quiet --disable-pip-version-check
if !errorlevel! neq 0 (
    echo [!] Failed to install/update requirements
    echo Showing detailed output:
    echo.
    pip install --upgrade -r requirements.txt --disable-pip-version-check
    if !errorlevel! neq 0 (
        echo.
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [#] IF YOU NEED HELP CONTACT THRU THE DISCORD DISCORD.GGG/SPAMMING
        echo [!] Critical dependency installation failure
        echo Common solutions:
        echo - Check internet connection
        echo - Run as administrator
        echo - Disable antivirus temporarily
        echo - Check requirements.txt for invalid packages
        pause
        exit /b 1
    )
)

echo [+] All dependencies installed/updated successfully
echo.
echo [*] Running main.py...
echo ==========================================
python main.py
goto :end

:python_install_guide
echo.
echo Step-by-step Python 3.12+ installation:
echo 1. Go to https://www.python.org/downloads/
echo 2. Click "Download Python 3.12.x" or newer
echo 3. Run the downloaded installer
echo 4. CRITICAL: Check "Add Python to PATH" checkbox
echo 5. Click "Install Now"
echo 6. Wait for installation to complete
echo 7. Restart your computer ^(recommended^)
echo 8. Run this script again
pause
exit /b 1

:end
endlocal
echo.
pause >nul
