# PDF to Image Converter

Convert PDF files to PNG images. Works as desktop app or right-click context menu.

## Usage

### Desktop Mode
1. Double-click `PDF2Image.exe`
2. Browse and select PDF file
3. Click "Convert PDF to Images"

### Context Menu Mode
1. **Setup once**: Right-click `install.bat` → "Run as administrator"
2. **Use**: Right-click any PDF → "Convert to Images"
3. **Remove**: Right-click `uninstall.bat` → "Run as administrator"

## Output
Images saved as `filename_page_001.png` in same folder as PDF.

## Files
- `PDF2Image.exe` - Main application  
- `install.bat` - Add context menu
- `uninstall.bat` - Remove context menu

## Requirements
- Windows
- Admin privileges (context menu only)
- No Python needed

---

## For Developers

### Build
```bash
pip install -r requirements.txt
build.bat
```

### Files
- `main.py` - Source code
- `requirements.txt` - Dependencies  
- `build.bat` - Build script