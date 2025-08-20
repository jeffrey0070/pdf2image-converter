# PDF2Image v2 Enhancement Tasks

## Overview
Enhance the PDF to Image converter with context menu integration and modern UI/UX improvements in two phases.

## Phase 1: Core Context Menu Integration

### Goal
Deliver functional context menu integration with minimal changes to existing application.

### Phase 1.1. Command-Line Argument Support for Context Menu Integration
**Status**: Pending
**Description**: Enable the GUI app to accept PDF file paths as command-line arguments for context menu integration.

**Implementation Details**:
- Modify `main.py` to check `sys.argv` for PDF file path
- If argument provided, auto-populate the file selection
- Update `self.pdf_path` and `self.pdf_label` on startup
- Optional: Add auto-convert flag for immediate processing
- Ensure GUI remains open after context menu conversion

**Files to Modify**:
- `main.py` - Add argument parsing in `__init__` method

### Phase 1.2. Update Output Logic to Same Folder as PDF
**Status**: Pending
**Description**: Change output from fixed C:\Temp to same folder as source PDF file.

**Implementation Details**:
- Remove fixed C:\Temp output path
- Save images in same directory as source PDF
- Use PDF filename as image prefix
- No need for output folder selection UI

**File Naming Convention**:
- Format: `filename_page_001.png`, `filename_page_002.png`, etc.
- Uses PDF filename as prefix (without .pdf extension)
- Save images in same folder as PDF file

**UI Changes**:
- Remove output folder display and browse button
- Update status messages to show "Images saved to PDF folder"
- Simplify UI layout without output folder controls

**Files to Modify**:
- `main.py` - Update conversion logic to use PDF's directory

### Phase 1.3. Create Installer/Uninstaller for Context Menu
**Status**: Pending
**Description**: Create Windows Registry installer and uninstaller for context menu integration.

**Implementation Details**:
- **install.bat**: Add Windows Registry entries for PDF context menu
- **uninstaller.bat**: Remove Registry entries cleanly
- Support major PDF handlers (Edge, Chrome, Adobe)
- Require Administrator privileges
- Point Registry entries to main executable

**Registry Targets**:
- MSEdgePDF (Microsoft Edge)
- AcroExch.Document.DC (Adobe Reader/Acrobat)
- ChromeHTML and Chrome.PDF (Google Chrome)

**Files to Create**:
- `install.bat` - Context menu installer
- `uninstall.bat` - Context menu removal
- Update `build.bat` to copy installer files to dist/

**Registry Command Format**:
```
reg add "HKEY_CLASSES_ROOT\MSEdgePDF\shell\ConvertToImages\command" /ve /t REG_SZ /d "\"%EXECUTABLE_PATH%\" \"%%1\"" /f
```

### Phase 1.4. Test Both GUI Modes
**Status**: Pending
**Description**: Thoroughly test standalone GUI and context menu integration.

**Testing Scenarios**:
- **Standalone mode**: Double-click executable, normal usage
- **Context menu mode**: Right-click PDF → "Convert to Images"
- **Drag-drop testing**: Single and multiple file drops
- **Error scenarios**: Invalid files, permission issues
- **Edge cases**: Very large PDFs, corrupted files

**Test Cases**:
- Launch without arguments (normal GUI mode)
- Launch with PDF argument (context menu mode)
- Drag valid PDF files
- Drag invalid files (non-PDF)
- Convert with various output folders
- Test UI responsiveness during conversion

---

## Phase 2: UI/UX Enhancements

### Goal
Modernize the GUI with better styling and drag-drop functionality.

### Phase 2.1. Enhance GUI UI/UX with Modern Styling
**Status**: Pending
**Description**: Modernize the GUI appearance and user experience.

**UI/UX Improvements**:
- **Window sizing**: Increase to ~500x350 for better layout
- **Color scheme**: Modern color palette (blues, grays, whites)
- **Typography**: Better font choices and sizing
- **Spacing**: Improved padding and margins
- **Visual hierarchy**: Clear sections and grouping
- **Button styling**: Modern flat design with hover effects
- **Progress indicators**: Progress bar during conversion
- **Status messages**: Better formatted status updates

**Layout Enhancements**:
- Group related elements in frames
- Add visual separators between sections
- Improve button placement and sizing
- Better alignment and spacing

**Files to Modify**:
- `main.py` - Enhance `setup_ui()` method with modern styling

### Phase 2.2. Implement Drag-and-Drop Functionality
**Status**: Pending
**Description**: Add drag-and-drop support for PDF files to improve user experience.

**Implementation Details**:
- Create drag-drop target area in GUI
- Add visual feedback when dragging over drop zone
- Validate dropped files (PDF only)
- Support single and multiple file drops
- Update file selection display after successful drop
- Add hover effects and visual indicators

**Technical Requirements**:
- Use `tkinterdnd2` library for drag-drop support
- Add to `requirements.txt`
- Implement drop event handlers
- File type validation (.pdf extension)

**Files to Modify**:
- `main.py` - Add drag-drop handlers and UI elements
- `requirements.txt` - Add tkinterdnd2 dependency

### Phase 2.3. Comprehensive Testing
**Status**: Pending
**Description**: Test all Phase 2 enhancements with existing Phase 1 functionality.

**Testing Focus**:
- Modern UI elements work correctly
- Drag-drop functionality is smooth and intuitive
- All features work together (context menu + UI + drag-drop)
- Performance testing with enhanced UI

---

## Implementation Order

### Phase 1 (Priority)
1. Command-line argument support (enables context menu)
2. Update output logic to same folder as PDF
3. Create installer/uninstaller for context menu
4. Test both GUI modes

### Phase 2 (Enhancement)
1. Enhance GUI UI/UX with modern styling
2. Implement drag-and-drop functionality
3. Comprehensive testing

## Technical Notes
- Maintain simplicity philosophy (minimal dependencies)
- Keep total codebase under 150 lines if possible
- Focus on Windows environment
- Use existing libraries efficiently
- Ensure single executable works for both modes

## Success Criteria
- ✅ Single executable supports both standalone and context menu usage
- ✅ Modern, intuitive GUI interface
- ✅ Drag-drop functionality works smoothly
- ✅ Users can choose output location
- ✅ GUI remains open after context menu conversion
- ✅ All existing functionality preserved