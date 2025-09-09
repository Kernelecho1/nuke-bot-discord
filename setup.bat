@echo off
echo ================================
echo Installation automatique du bot
echo ================================

echo Verification de Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installe ou n'est pas dans le PATH
    echo Telechargement et installation de Python...
    
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe' -OutFile 'python-installer.exe'}"
    
    echo Installation de Python en cours...
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    echo Attente de la fin de l'installation...
    timeout /t 30 /nobreak >nul
    
    del python-installer.exe
    
    echo Python installe avec succes!
    echo Redemarrage necessaire pour mettre a jour le PATH
    pause
    exit
) else (
    echo Python est deja installe
    python --version
)

echo.
echo Verification des dependances...

echo Installation de colorama...
pip install colorama --quiet
if %errorlevel% neq 0 (
    echo Erreur lors de l'installation de colorama
    pause
    exit /b 1
)

echo Installation de discord.py...
pip install discord.py --quiet
if %errorlevel% neq 0 (
    echo Erreur lors de l'installation de discord.py
    pause
    exit /b 1
)

echo.
echo ================================
echo Installation terminee avec succes!
echo ================================
echo.

echo Recherche de toolraid.py...
for /r "C:\" %%f in (toolraid.py) do (
    set "toolraid=%%f"
    goto :found
)

echo Erreur: toolraid.py introuvable sur le disque.
pause
exit /b 1

:found
echo Fichier trouve: %toolraid%
echo Lancement de toolraid.py...
python "%toolraid%"

pause
