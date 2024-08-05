import os
from PyPDF2 import PdfReader

# Directory containing PDF files
pdf_dir = 'files'
# Directory to save text files
txt_dir = 'text_files'
os.makedirs(txt_dir, exist_ok=True)

# Function to convert a single PDF to text
def convert_pdf_to_txt(pdf_path, txt_path):
    try:
        # Open and read the PDF file
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            text_content = ""

            # Iterate through each page in the PDF
            for page in pdf_reader.pages:
                text_content += page.extract_text()

        # Write the extracted text to a text file
        with open(txt_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)

        print(f"Successfully converted {pdf_path} to {txt_path}")

    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")

# Iterate through all PDF files in the directory
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_dir, filename)
        txt_filename = f"{os.path.splitext(filename)[0]}.txt"
        txt_path = os.path.join(txt_dir, txt_filename)

        # Convert PDF to text
        convert_pdf_to_txt(pdf_path, txt_path)
