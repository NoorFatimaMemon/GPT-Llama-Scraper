@echo off

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
) else (
    :: Set the version of Python to install
    set PYTHON_VERSION=3.10.0

    :: Download and install Python
    echo Downloading Python %PYTHON_VERSION%...
    curl -o python_installer.exe https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe
    echo Installing Python %PYTHON_VERSION%...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    :: Add Python to PATH (if not added automatically)
    set "PATH=%PATH%;C:\Program Files\Python310;C:\Program Files\Python310\Scripts"
)

:: Verify Python installation
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python installation failed. Exiting...
    exit /b 1
)

:: Install pip if it is not already installed
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
)

:: Install requirements
echo Installing requirements...
pip install -r requirements.txt

:: Start the Download LLAMA script
start "Download LLAMA Script" python llama_download.py
echo script is started.

pause