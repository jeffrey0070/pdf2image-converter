@echo off
echo Building PDF2Image converter...
pip install pyinstaller
pyinstaller --onefile --windowed --name="PDF2Image" --icon=NONE main.py

echo.
echo Copying distribution files to dist folder...
copy install.bat dist\
copy uninstall.bat dist\
copy README.md dist\

echo.
echo Build complete! Distribution files in dist folder:
echo   - PDF2Image.exe (main application)
echo   - install.bat (context menu installer)
echo   - uninstall.bat (context menu remover)
echo   - README.md (user instructions)
pause