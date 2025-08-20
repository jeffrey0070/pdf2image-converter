@echo off
echo PDF to Image Context Menu Uninstaller
echo.

REM Check for admin privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Must be run as Administrator
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo Removing context menu from all PDF handlers...

reg delete "HKEY_CLASSES_ROOT\MSEdgePDF\shell\ConvertToImages" /f 2>nul
reg delete "HKEY_CLASSES_ROOT\AcroExch.Document.DC\shell\ConvertToImages" /f 2>nul
reg delete "HKEY_CLASSES_ROOT\ChromeHTML\shell\ConvertToImages" /f 2>nul
reg delete "HKEY_CLASSES_ROOT\Chrome.PDF\shell\ConvertToImages" /f 2>nul

echo SUCCESS: Context menu removed

pause