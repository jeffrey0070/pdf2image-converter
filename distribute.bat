@echo off
echo ========================================
echo PDF2Image Distribution Builder
echo ========================================

REM Read version from version.py
for /f "tokens=*" %%a in ('python -c "from version import __version__; print(__version__)"') do set VERSION=%%a
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
echo Step 3: Create GitHub release manually...
echo.
echo ✅ Distribution package ready: PDF2Image-v%VERSION%.zip
echo.
echo To create GitHub release:
echo 1. Go to: https://github.com/jeffrey0070/pdf2image-converter/releases
echo 2. Click "Create a new release"
echo 3. Tag: v%VERSION%
echo 4. Title: PDF2Image v%VERSION%
echo 5. Upload: PDF2Image-v%VERSION%.zip
echo 6. Click "Publish release"

cd ..
echo.
echo ========================================
echo Distribution complete!
echo Package: dist\PDF2Image-v%VERSION%.zip
echo ========================================
pause