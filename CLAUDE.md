# Project Context for Claude Code

## User Preferences & Development Philosophy

### Simplicity First
- **Ultra-minimal codebase**: ~176 lines total (achieved!)
- **Few dependencies**: Only PyMuPDF and Pillow
- **Personal use only**: No enterprise features or complex error handling
- **Safe environment**: Development is for personal use in trusted settings

### Technical Preferences
- **Python + Tkinter**: Chosen for simplicity and minimal dependencies
- **Leverage existing libraries**: PyMuPDF and Pillow for PDF processing
- **Windows-focused**: Primary development and usage environment
- **No over-engineering**: Avoid complex patterns, just functional code

### Development Approach
- **Incremental**: Build in small, working phases - COMPLETED Phase 1 & 2
- **Practical**: Focus on "it works" over "it's perfect"
- **Ultra-minimal UI**: Drop zone + 3 other essential elements only
- **Direct implementation**: Skip advanced architecture patterns

### Current Status (v2.0.2)
- **Phase 1**: Context menu integration ✅
- **Phase 2**: Ultra-minimal UI design ✅
- **Performance optimization**: Lazy loading of heavy libraries ✅
- **Future**: Drag-drop support when stable libraries available

### Performance Optimizations Applied
- **Lazy imports**: PyMuPDF and Pillow now load only during conversion (not startup)
- **Removed auto-resize**: Eliminated window geometry calculations for filename display
- **Expected result**: ~50% faster startup time

### Project Files
- `requirements.txt` - Python dependencies (PyMuPDF, Pillow)
- `development-plan-v1.md` - Historical: v1.0.0 development plan and achievements
- `development-plan-v2.md` - Current: v2.0.0 development tasks and completion status

## GitHub Repository Settings
- **Repository URL**: https://github.com/jeffrey0070/pdf2image-converter.git
- **Owner**: jeffrey0070
- **Access**: Full access via gh CLI configured

## Testing Philosophy
- **Manual testing preferred**: Claude should provide test instructions/scenarios, not run tests automatically
- **User-controlled**: User prefers to execute tests manually for full control
- **Test guidance only**: Claude provides what to test, user performs the actual testing

## Key Constraints
- Keep it extremely simple
- Minimize code maintenance burden
- Focus on core functionality only
- No need for advanced features or robust error handling