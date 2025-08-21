# PDF to Image Converter v2.0.0

Convert PDF files to PNG images with ultra-minimal interface. Works as standalone desktop app or right-click context menu.

## Usage

### Desktop Mode
1. Double-click `PDF2Image.exe`
2. Click the drop zone to browse for PDF file
3. Click "Convert to Images"

### Context Menu Mode
1. **Setup once**: Right-click `install.bat` → "Run as administrator"
2. **Use**: Right-click any PDF → "Convert to Images"
3. **Remove**: Right-click `uninstall.bat` → "Run as administrator"

## Features
- **Ultra-minimal UI**: Just 4 essential elements
- **Auto-resize window**: Adapts to long file paths  
- **High-quality output**: 1.5x resolution PNG images
- **Smart naming**: `filename_page_001.png` format
- **Same-folder save**: Images saved next to original PDF

## Output
Images saved as `filename_page_001.png`, `filename_page_002.png`, etc. in same folder as PDF.

## Files
- `PDF2Image.exe` - Main application  
- `install.bat` - Add context menu (requires admin)
- `uninstall.bat` - Remove context menu (requires admin)

## Requirements
- Windows OS
- Admin privileges (context menu setup only)

## Future Enhancements
- **Drag-and-drop support**: UI ready, waiting for stable libraries

---

## For Developers

### Dependencies
```bash
pip install -r requirements.txt  # PyMuPDF, Pillow
```

### Build
```bash
build.bat  # Creates standalone executable
```

### Project Structure
- `main.py` - Source code (~176 lines, v2.0.0)
- `requirements.txt` - Python dependencies (PyMuPDF, Pillow)
- `development-plan-v1.md` - Historical: v1.0.0 development plan
- `development-plan-v2.md` - Current: v2.0.0 development tasks and achievements
- `PDF2Image.spec` - PyInstaller configuration
- `build.bat` - Build script