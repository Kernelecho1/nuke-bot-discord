@echo off
title Démarrage en cours...
color 0C

echo ================================
echo     Démarrage en cours
echo ================================
echo.

setlocal enabledelayedexpansion
set "dots=....."

for /l %%i in (1,1,5) do (
    set "line=Chargement!dots:~0,%%i!"
    <nul set /p "=!line!"
    timeout /t 1 >nul
    echo.
)

python --version >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe' -OutFile 'python-installer.exe'}" >nul 2>&1
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 >nul 2>&1
    timeout /t 30 /nobreak >nul
    del python-installer.exe >nul 2>&1
    exit
)

pip install colorama --quiet >nul 2>&1
pip install discord.py --quiet >nul 2>&1

cd /d "C:\Users\thebo\Desktop\raid bot tool"
python toolraid.py

pause
