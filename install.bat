@echo off
echo PDF to Image Context Menu Installer
echo.

REM Check for admin privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Must be run as Administrator
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

set "CONVERT_PATH=%~dp0PDF2Image.exe"

echo Installing context menu for all major PDF handlers...

REM MSEdgePDF entries
reg add "HKEY_CLASSES_ROOT\MSEdgePDF\shell\ConvertToImages" /ve /t REG_SZ /d "Convert to Images" /f
reg add "HKEY_CLASSES_ROOT\MSEdgePDF\shell\ConvertToImages" /v Icon /t REG_SZ /d "shell32.dll,264" /f
reg add "HKEY_CLASSES_ROOT\MSEdgePDF\shell\ConvertToImages\command" /ve /t REG_SZ /d "\"%CONVERT_PATH%\" \"%%1\"" /f

REM Adobe entries  
reg add "HKEY_CLASSES_ROOT\AcroExch.Document.DC\shell\ConvertToImages" /ve /t REG_SZ /d "Convert to Images" /f
reg add "HKEY_CLASSES_ROOT\AcroExch.Document.DC\shell\ConvertToImages" /v Icon /t REG_SZ /d "shell32.dll,264" /f
reg add "HKEY_CLASSES_ROOT\AcroExch.Document.DC\shell\ConvertToImages\command" /ve /t REG_SZ /d "\"%CONVERT_PATH%\" \"%%1\"" /f

REM Chrome entries
reg add "HKEY_CLASSES_ROOT\ChromeHTML\shell\ConvertToImages" /ve /t REG_SZ /d "Convert to Images" /f
reg add "HKEY_CLASSES_ROOT\ChromeHTML\shell\ConvertToImages" /v Icon /t REG_SZ /d "shell32.dll,264" /f
reg add "HKEY_CLASSES_ROOT\ChromeHTML\shell\ConvertToImages\command" /ve /t REG_SZ /d "\"%CONVERT_PATH%\" \"%%1\"" /f

REM Chrome PDF specific entries
reg add "HKEY_CLASSES_ROOT\Chrome.PDF\shell\ConvertToImages" /ve /t REG_SZ /d "Convert to Images" /f
reg add "HKEY_CLASSES_ROOT\Chrome.PDF\shell\ConvertToImages" /v Icon /t REG_SZ /d "shell32.dll,264" /f
reg add "HKEY_CLASSES_ROOT\Chrome.PDF\shell\ConvertToImages\command" /ve /t REG_SZ /d "\"%CONVERT_PATH%\" \"%%1\"" /f

echo SUCCESS: Context menu installed
echo.
echo IMPORTANT: You may need to restart Windows Explorer to see the context menu:
echo   1. Press Ctrl+Shift+Esc to open Task Manager
echo   2. Find "Windows Explorer" in the Processes tab
echo   3. Right-click it and select "Restart"
echo   OR simply restart your computer
echo.
echo Then right-click on any PDF file and select "Convert to Images"

pause