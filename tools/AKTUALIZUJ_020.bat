@echo off
setlocal
title Bogowie Pamietaja - aktualizacja 0.2.0 DEV
echo.
echo   BOGOWIE PAMIETAJA - 0.2.0 DEV, wersja skrocona
echo   Nadpisanie istniejacego moda na dysku H
echo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0INSTALL_020_NADPISZ.ps1"
set "RC=%ERRORLEVEL%"
echo.
if not "%RC%"=="0" (
  echo   BLAD AKTUALIZACJI. Sprawdz komunikat powyzej.
) else (
  echo   OK. Wlacz ten sam mod w launcherze CK3.
)
echo.
pause
exit /b %RC%
