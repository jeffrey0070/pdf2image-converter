import tkinter as tk
from tkinter import filedialog, messagebox
import os
import fitz  # PyMuPDF
from PIL import Image

class PDF2ImageConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF to Image Converter")
        self.root.geometry("400x200")
        
        self.pdf_path = None
        self.output_folder = r"C:\Temp"
        
        self.setup_ui()
        
    def setup_ui(self):
        # PDF selection
        tk.Label(self.root, text="Select PDF file:").pack(pady=5)
        self.pdf_button = tk.Button(self.root, text="Browse PDF", command=self.select_pdf)
        self.pdf_button.pack(pady=5)
        
        self.pdf_label = tk.Label(self.root, text="No PDF selected", fg="gray")
        self.pdf_label.pack(pady=2)
        
        # Output info
        tk.Label(self.root, text="Images will be saved to C:\\Temp", fg="blue").pack(pady=10)
        
        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert PDF to Images", 
                                      command=self.convert_pdf, bg="lightblue")
        self.convert_button.pack(pady=10)
        
        # Status
        self.status_label = tk.Label(self.root, text="Ready", fg="green")
        self.status_label.pack(pady=5)
        
        
    def select_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf")]
        )
        if file_path:
            self.pdf_path = file_path
            self.pdf_label.config(text=os.path.basename(file_path), fg="black")
            
            
    def convert_pdf(self):
        if not self.pdf_path:
            messagebox.showerror("Error", "Please select a PDF file")
            return
            
        # Create C:\Temp if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)
            
        try:
            self.status_label.config(text="Converting...", fg="orange")
            self.root.update()
            
            pdf_document = fitz.open(self.pdf_path)
            page_count = len(pdf_document)
            
            for page_num in range(page_count):
                page = pdf_document.load_page(page_num)
                # Increase resolution with matrix scaling (1.5x bigger)
                mat = fitz.Matrix(1.5, 1.5)
                pix = page.get_pixmap(matrix=mat)
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                
                image_path = os.path.join(self.output_folder, f"page_{page_num + 1:03d}.png")
                img.save(image_path, "PNG")
                
            pdf_document.close()
                
            self.status_label.config(text=f"Converted {page_count} pages successfully!", fg="green")
            messagebox.showinfo("Success", f"Converted {page_count} pages to {self.output_folder}")
            
        except Exception as e:
            self.status_label.config(text="Error occurred", fg="red")
            messagebox.showerror("Error", f"Failed to convert PDF: {str(e)}")
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PDF2ImageConverter()
    app.run()