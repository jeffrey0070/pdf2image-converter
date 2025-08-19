@echo off
echo Building PDF2Image converter...
pip install pyinstaller
pyinstaller --onefile --windowed --name="PDF2Image" --icon=NONE main.py
echo.
echo Build complete! Check dist folder for PDF2Image.exe
pause