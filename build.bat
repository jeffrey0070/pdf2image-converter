@echo off
echo Building PDF2Image converter...
pip install pyinstaller
pyinstaller --onedir --windowed --name="PDF2Image" --icon=NONE --noupx main.py

echo.
echo Copying distribution files to dist\PDF2Image folder...
copy install.bat dist\PDF2Image\
copy uninstall.bat dist\PDF2Image\
copy README.txt dist\PDF2Image\

echo.
echo Build complete! Distribution files in dist\PDF2Image folder:
echo   - PDF2Image.exe (main application)
echo   - install.bat (context menu installer)
echo   - uninstall.bat (context menu remover)
echo   - README.txt (user instructions)
echo   - Plus all required DLLs and runtime files
pause