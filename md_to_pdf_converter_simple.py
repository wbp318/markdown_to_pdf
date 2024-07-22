import tkinter as tk
from tkinter import filedialog, messagebox
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
import os
import subprocess

class MarkdownToPDFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Markdown to PDF Converter")
        master.geometry("400x200")
        master.resizable(False, False)

        self.label = tk.Label(master, text="Convert Markdown to PDF", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.select_button = tk.Button(master, text="Select Markdown File", command=self.select_file)
        self.select_button.pack(pady=10)

        self.convert_button = tk.Button(master, text="Convert and Open PDF", command=self.convert_file, state=tk.DISABLED)
        self.convert_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=10)

        self.file_path = None

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Markdown Files", "*.md")])
        if self.file_path:
            self.status_label.config(text=f"Selected: {os.path.basename(self.file_path)}")
            self.convert_button.config(state=tk.NORMAL)

    def convert_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if not output_file:
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                markdown_text = f.read()
            
            # Create PDF using ReportLab
            doc = SimpleDocTemplate(output_file, pagesize=letter)
            styles = getSampleStyleSheet()
            
            code_style = ParagraphStyle(
                'CodeStyle',
                parent=styles['Code'],
                fontSize=10,
                leading=14,
                leftIndent=20,
                firstLineIndent=-20,
                alignment=TA_LEFT
            )

            flowables = []
            lines = markdown_text.split('\n')
            for i, line in enumerate(lines, 1):
                numbered_line = f"{i:2d} {line}"
                p = Paragraph(numbered_line, code_style)
                flowables.append(p)
                flowables.append(Spacer(1, 2))

            doc.build(flowables)

            self.status_label.config(text="Conversion complete")
            messagebox.showinfo("Success", f"Converted {os.path.basename(self.file_path)} to PDF")
            
            # Open the PDF file with the default viewer
            os.startfile(output_file)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="Conversion failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownToPDFConverter(root)
    root.mainloop()