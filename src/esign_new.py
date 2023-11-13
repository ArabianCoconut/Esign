import glob
import os
import time
import img2pdf
from PIL import Image
from pdf2jpg import pdf2jpg

PDF_HERE_DIR = 'PDF_Here'
PDF_SIGNED_DIR = 'PDF_Signed'
SIGNATURE_PATH = './signature.png'
SIGNATURE_SIZE = (800, 800)
SIGNATURE_POSITION = (450, 2100)

def esign():
    """
    This function signs all PDF files in the 'PDF_Here' directory using a signature image and saves the signed PDFs in the 'PDF_Signed' directory.
    """
    try:
        # Get the paths of all PDF files in the 'PDF_Here' directory
        pdf_paths = glob.glob(f'{PDF_HERE_DIR}/*.pdf')

        for pdf_path in pdf_paths:
            # Convert the PDF to JPG
            jpg_path = pdf2jpg.convert_pdf2jpg(pdf_path, outputpath=PDF_SIGNED_DIR, pages='ALL')[0]['output_jpgfiles'][0]

            # Open the JPG as a PIL Image
            background = Image.open(jpg_path)

            # Open the signature image and resize it
            signature = Image.open(SIGNATURE_PATH).convert('RGBA')
            signature_resized = signature.resize(SIGNATURE_SIZE)

            # Paste the signature onto the background
            background.paste(signature_resized, SIGNATURE_POSITION, signature_resized)

            # Save the signed PDF
            background.save(jpg_path)

    except FileNotFoundError:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write("Error: No PDF files found.\n"
            f"Please place the PDF files in the '{PDF_HERE_DIR}' directory.\n")
        time.sleep(5)
        exit(0)

