import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
import fitz  # PyMuPDF
from PIL import Image

class PDF2ImageConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF to Image Converter v2.0.0 - Jeffrey Wang")
        self.root.geometry("450x280")
        self.root.minsize(450, 180)  # Set minimum size
        self.root.configure(bg="#ffffff")
        
        self.pdf_path = None
        
        # Check for command-line argument (context menu integration)
        if len(sys.argv) > 1:
            self.pdf_path = sys.argv[1]
        
        self.setup_ui()
        
        # Auto-convert if PDF provided via command line
        if self.pdf_path:
            # Schedule conversion to run after GUI is fully initialized
            self.root.after(100, self.convert_pdf)
            
    def show_message(self, msg_type, title, message):
        """Show message box centered on main window"""
        # Create a custom dialog centered on main window
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.resizable(False, False)
        dialog.grab_set()  # Make it modal
        
        # Calculate position relative to main window
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_width = self.root.winfo_width()
        main_height = self.root.winfo_height()
        
        dialog_width = 300
        dialog_height = 120
        
        # Center on main window
        x = main_x + (main_width - dialog_width) // 2
        y = main_y + (main_height - dialog_height) // 2
        
        dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")
        dialog.configure(bg="#ffffff")
        
        # Add message content
        frame = tk.Frame(dialog, bg="#ffffff", padx=20, pady=20)
        frame.pack(fill="both", expand=True)
        
        # Icon and message
        icon = "⚠️" if msg_type == "error" else "✅"
        msg_label = tk.Label(frame, text=f"{icon} {message}", 
                            font=("Segoe UI", 10), bg="#ffffff", fg="#333333",
                            wraplength=260, justify="center")
        msg_label.pack(pady=(0, 15))
        
        # OK button
        ok_button = tk.Button(frame, text="OK", command=dialog.destroy,
                             font=("Segoe UI", 10), bg="#0066cc", fg="white",
                             padx=20, pady=5, relief="flat")
        ok_button.pack()
        ok_button.focus_set()
        
        # Bind Enter key to close
        dialog.bind('<Return>', lambda e: dialog.destroy())
        dialog.bind('<Escape>', lambda e: dialog.destroy())
        
        # Wait for dialog to close
        dialog.wait_window()
        
    def setup_ui(self):
        # Main container with minimal padding
        main_frame = tk.Frame(self.root, bg="#ffffff", padx=30, pady=25)
        main_frame.pack(fill="both", expand=True)
        
        # File selection label
        tk.Label(main_frame, text="Select PDF File:", font=("Segoe UI", 10), 
                bg="#ffffff", fg="#333333").pack(anchor="w", pady=(0, 8))
        
        # Clickable drop zone rectangle (future: will support drag-drop functionality)
        self.drop_zone = tk.Frame(main_frame, bg="#f8f8f8", relief="solid", bd=1)
        self.drop_zone.pack(fill="x", pady=(0, 20))
        self.drop_zone.bind("<Button-1>", lambda e: self.select_pdf())
        
        # Text inside drop zone (shows filename when selected)
        if self.pdf_path:
            display_text = f"Click here to browse for PDF file\n\n{self.pdf_path}"
        else:
            display_text = "Click here to browse for PDF file"
            
        self.drop_text = tk.Label(self.drop_zone, text=display_text, 
                                 font=("Segoe UI", 9), bg="#f8f8f8", fg="#666666",
                                 justify="center", wraplength=350, pady=10)
        self.drop_text.pack(pady=10)
        self.drop_text.bind("<Button-1>", lambda e: self.select_pdf())
        
        # Simple info line
        tk.Label(main_frame, text="Images will be saved to the same folder as the PDF", 
                font=("Segoe UI", 9), bg="#ffffff", fg="#666666").pack(pady=(0, 25))
        
        # Convert button
        self.convert_button = tk.Button(main_frame, text="Convert to Images", command=self.convert_pdf,
                                       font=("Segoe UI", 11), bg="#0066cc", fg="white",
                                       padx=25, pady=10, relief="flat")
        self.convert_button.pack()

    def select_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            self.pdf_path = file_path
            self.drop_text.config(text=f"Click here to browse for PDF file\n\n{file_path}")
            # Auto-resize window if needed for long filename
            self.root.update_idletasks()
            required_height = self.root.winfo_reqheight()
            current_height = self.root.winfo_height()
            if required_height > current_height:
                self.root.geometry(f"450x{required_height + 15}")

    def convert_pdf(self):
        if not self.pdf_path:
            self.show_message("error", "Error", "Please select a PDF file")
            return
            
        # Validate file exists and is PDF
        if not os.path.exists(self.pdf_path):
            self.show_message("error", "Error", f"File not found: {self.pdf_path}")
            return
            
        if not self.pdf_path.lower().endswith('.pdf'):
            self.show_message("error", "Error", f"Not a PDF file: {self.pdf_path}")
            return
            
        # Use same folder as PDF file
        output_folder = os.path.dirname(self.pdf_path)
        pdf_basename = os.path.splitext(os.path.basename(self.pdf_path))[0]

        try:
            pdf_document = fitz.open(self.pdf_path)
            page_count = len(pdf_document)
            
            for page_num in range(page_count):
                page = pdf_document.load_page(page_num)
                # Increase resolution with matrix scaling (1.5x bigger)
                mat = fitz.Matrix(1.5, 1.5)
                pix = page.get_pixmap(matrix=mat)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                
                # Use PDF filename as prefix: filename_page_001.png
                image_filename = f"{pdf_basename}_page_{page_num + 1:03d}.png"
                image_path = os.path.join(output_folder, image_filename)
                img.save(image_path, "PNG")
            pdf_document.close()
            
            # Show success message
            self.show_message("info", "Success", f"Converted {page_count} pages to PDF folder")
            
        except Exception as e:
            # Show error message
            self.show_message("error", "Error", f"Failed to convert PDF: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PDF2ImageConverter()
    app.run()