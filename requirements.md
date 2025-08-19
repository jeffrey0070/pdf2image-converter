# PDF to Image Converter - Requirements

## Purpose
Personal use PDF to image converter with minimal codebase.

## Features
- Browse and select PDF file
- Convert all pages to PNG images
- Save to C:\Temp folder automatically
- Simple Tkinter GUI (2-3 buttons max)

## Technical Stack
- **Language**: Python 3.8+
- **GUI**: Tkinter (built-in)
- **PDF Processing**: pdf2image library
- **Image Handling**: Pillow (PIL)
- **Drag-Drop**: tkinterdnd2

## Constraints
- Target: 50-100 lines of code total
- Minimal dependencies (3-4 libraries max)
- Windows-only (personal use)
- No advanced features or settings
- No error handling complexity

## Success Criteria
- Opens PDF files via drag-drop or file dialog
- Converts to PNG images (page_001.png, page_002.png, etc.)
- Saves to user-selected folder
- Works reliably for typical PDF files