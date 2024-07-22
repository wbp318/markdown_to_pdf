# Markdown to PDF Converter

This application converts Markdown files to PDF format with a simple graphical user interface. It's designed to be easy to use and doesn't require any technical knowledge.

## Features

- Convert Markdown (.md) files to PDF format
- Simple and intuitive graphical user interface
- Automatically opens the generated PDF after conversion
- Preserves line numbers from the original Markdown file
- Standalone executable available for Windows users

## How to Use

1. Download the `markdown_to_pdf_converter.exe` file from the [Releases](link-to-your-releases-page) section.
2. Double-click the executable to run the application.
3. Click "Select Markdown File" to choose your .md file.
4. Click "Convert and Open PDF" to generate the PDF.
5. Choose where to save your PDF file.
6. The generated PDF will automatically open in your default PDF viewer.

## For Developers

If you want to run the script directly or contribute to the project:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/markdown-to-pdf-converter.git
   ```
2. Install the required dependencies:
   ```
   pip install markdown reportlab
   ```
3. Run the script:
   ```
   python md_to_pdf_converter_simple.py
   ```

## Building the Executable

To build the executable yourself:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
2. Run the following command:
   ```
   pyinstaller --onefile --windowed md_to_pdf_converter_simple.py
   ```
3. Find the executable in the `dist` folder.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
