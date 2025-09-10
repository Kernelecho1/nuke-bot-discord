@echo off
title Démarrage du bot

for /f "tokens=2 delims=: " %%i in ('"prompt $H & for %%b in (1) do rem"') do set "BS=%%i"
set "ESC="
for /F "delims=" %%a in ('echo prompt $E ^| cmd') do set "ESC=%%a"

:anim
cls
echo %ESC%[31mDémarrage en cours.
ping -n 2 localhost >nul
cls
echo %ESC%[31mDémarrage en cours..
ping -n 2 localhost >nul
cls
echo %ESC%[31mDémarrage en cours...
ping -n 2 localhost >nul
goto anim
