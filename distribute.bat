@echo off
echo ========================================
echo PDF2Image Distribution Builder
echo ========================================

REM Read version from version.txt
set /p VERSION=<version.txt
echo Version: %VERSION%

echo.
echo Step 1: Building application...
call build.bat

if not exist "dist\PDF2Image\PDF2Image.exe" (
    echo ERROR: Build failed - PDF2Image.exe not found
    pause
    exit /b 1
)

echo.
echo Step 2: Creating distribution package...
cd dist
if exist "PDF2Image-v%VERSION%.zip" del "PDF2Image-v%VERSION%.zip"
powershell -command "Compress-Archive -Path 'PDF2Image' -DestinationPath 'PDF2Image-v%VERSION%.zip'"

if not exist "PDF2Image-v%VERSION%.zip" (
    echo ERROR: Failed to create zip file
    cd ..
    pause
    exit /b 1
)

echo ✅ Created: PDF2Image-v%VERSION%.zip

echo.
echo Step 3: GitHub release options...
echo [1] Create GitHub release (requires gh CLI)
echo [2] Skip GitHub release
set /p CHOICE="Choose option (1 or 2): "

if "%CHOICE%"=="1" (
    echo.
    echo Creating GitHub release v%VERSION%...
    gh release create v%VERSION% "PDF2Image-v%VERSION%.zip" --title "PDF2Image v%VERSION%" --notes "Release v%VERSION%"
    if %ERRORLEVEL%==0 (
        echo ✅ GitHub release created successfully
    ) else (
        echo ❌ GitHub release failed - check gh CLI setup
    )
) else (
    echo ✅ Zip file ready for manual upload
)

cd ..
echo.
echo ========================================
echo Distribution complete!
echo Package: dist\PDF2Image-v%VERSION%.zip
echo ========================================
pause