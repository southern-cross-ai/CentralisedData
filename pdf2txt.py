import os
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text
from langchain.document_loaders import UnstructuredFileLoader
import nltk

# Download the necessary NLTK data
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('omw-1.4')

# Directory containing PDF files
pdf_dir = 'files'
# Directory to save text files
txt_dir = 'text_files'
os.makedirs(txt_dir, exist_ok=True)


def extract_text_with_langchain_pdf(pdf_path, txt_path):
    # check if the PDF file exists
    if not os.path.exists(pdf_path):
        print(f"The file {pdf_path} does not exist.")
        return

    # Get the name of the PDF file without extension to create the TXT filename
    pdf_file = os.path.basename(pdf_path)
    txt_filename = os.path.splitext(pdf_file)[0] + '.txt'

    # If txt_path is a directory, join it with the txt_filename
    if os.path.isdir(txt_path):
        txt_path = os.path.join(txt_path, txt_filename)

    # use the UnstructuredFileLoader to load the PDF file
    loader = UnstructuredFileLoader(pdf_path)
    documents = loader.load()
    pdf_pages_content = '\n'.join(doc.page_content for doc in documents)

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(pdf_pages_content)

    print(f"Extracted text from {pdf_file} and saved to {txt_path}")



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

def pdfminzer_pdf_to_txt(pdf_path, txt_path):
    try:
        text_content = extract_text(pdf_path)
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
        extract_text_with_langchain_pdf(pdf_path, txt_path)

