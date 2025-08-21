# PDF to Image Converter

Convert PDF files to high-quality PNG images with ultra-minimal interface. Supports desktop app and right-click context menu integration.

## Download

**[📥 Download Latest Release](https://github.com/jeffrey0070/pdf2image-converter/releases/latest)**

Extract the ZIP file and run `PDF2Image.exe` - no installation required.

## Quick Start

### Desktop Mode
1. Double-click `PDF2Image.exe`
2. Select PDF file
3. Click "Convert to Images"

### Context Menu (Optional)
- **Setup:** Right-click `install.bat` → Run as administrator
- **Use:** Right-click any PDF → "Convert to Images"
- **Remove:** Right-click `uninstall.bat` → Run as administrator

## Features

- **Ultra-minimal UI** - Just 4 essential elements
- **High-quality output** - 1.5x resolution PNG images  
- **Smart naming** - `filename_page_001.png` format
- **Same-folder save** - Images saved next to original PDF
- **Context menu integration** - Right-click any PDF to convert

## Requirements

- Windows OS
- Admin privileges (context menu setup only)

---

## For Developers

```bash
pip install -r requirements.txt
build.bat                 # Development build
distribute.bat           # Release package
```

**Version management:** Edit `version.py` - all files auto-update