import glob
import os
import time
import img2pdf
from PIL import Image
from pdf2jpg import pdf2jpg

PDF_HERE_DIR = 'src/PDF_Here'
PDF_SIGNED_DIR = 'src/PDF_Signed'
SIGNATURE_DIR = 'src/Signature_Sample'

SIGNATURE_SIZE = (800, 800)
SIGNATURE_POSITION = (450, 2100)

def log():
    '''
    Create a log file if there is no PDF files found.
    '''
    with open('log.txt', 'w', encoding='utf-8') as f:
            f.write(
                "Error: No PDF files found.\n"
                "Please place the PDF files in the 'PDF_Here' directory.\n"
                "Also, make sure the signature image is in the 'Signature_Sample' as this exe and with transparent background and in png format.\n"
            )
    time.sleep(5)
    exit(0)

def create_folders():
    """
    This function creates the 'PDF_Here', 'PDF_Signed', and 'Signature_Sample' directories if they don't exist.
    """
    try:
        os.mkdir(PDF_HERE_DIR)
        os.mkdir(PDF_SIGNED_DIR)
        os.mkdir(SIGNATURE_DIR)
    except FileExistsError:
        with open('log_warning.txt', 'w', encoding='utf-8') as f:
            f.write(
                "Warning: The 'PDF_Here', 'PDF_Signed',and 'Signature_Sample' directories already exist.\n"
                "Please delete them and run the program again. If the program do not work correctly.\n"
            )
    except FileNotFoundError:
        with open('Log_Error.txt', 'w', encoding='utf-8') as f:
            f.write(
                "Place .pdf files in the 'PDF_Here' directory.\n"
                "Place the signature image in the 'Signature_Sample' directory.\n"
            )

def esign():
    """
    This function signs all PDF files in the 'PDF_Here' directory using a signature image and saves the signed PDFs in the 'PDF_Signed' directory.
    """
    try:
        create_folders()
        # Get the paths of all PDF files in the 'PDF_Here' directory
        pdf_paths = glob.glob(f'{PDF_HERE_DIR}/*.pdf')
        signature_paths = glob.glob(f'{SIGNATURE_DIR}/*.png')[0]
        print(signature_paths)#* Debug
        for pdf_path in pdf_paths:
            # Convert the PDF to JPG
            jpg_path = pdf2jpg.convert_pdf2jpg(pdf_path, outputpath=PDF_SIGNED_DIR)[0]['output_jpgfiles'][0]

            # Open the JPG as a PIL Image
            background = Image.open(jpg_path)

            # Open the signature image and resize it
            signature = Image.open(signature_paths).convert('RGBA')
            signature_resized = signature.resize(SIGNATURE_SIZE)

            # Paste the signature onto the background
            background.paste(signature_resized, SIGNATURE_POSITION, signature_resized)

            # Save the signed PDF
            background.save(jpg_path, format='png', quality=100)

    except FileNotFoundError:
        log()
    except AttributeError:
        create_folders()
        
def convert_jpg_to_pdf():
    """
    This function converts all JPG files in the 'PDF_Signed' directory to PDF files and saves them in the same directory.
    """
    # Get all directories ending with '.pdf_dir'
    directories = glob.glob(f'{PDF_SIGNED_DIR}/*.pdf_dir')

    for directory in directories:
        # Get all '.pdf.jpg' files in the current directory
        jpg_files = glob.glob(f'{directory}/*.pdf.jpg')

        for jpg_file in jpg_files:
            # Convert '.pdf.jpg' to '.png'
            png_file = jpg_file.replace('.pdf.jpg', '.png')
            Image.open(jpg_file).save(png_file)

            # Convert '.png' to '.pdf'
            pdf_file = png_file.replace('.png', '.pdf')
            with open(png_file, 'rb') as img_file, open(pdf_file, 'wb') as pdf_file:
                pdf_bytes = img2pdf.convert(img_file.read())
                pdf_file.write(pdf_bytes)

            # Remove the '.png' and '.jpg' files
            os.remove(png_file)
            os.remove(jpg_file)

        # Rename files starting with '0_'
        for filename in glob.glob(f'{directory}/*.pdf'):
            if os.path.basename(filename).startswith('0_'):
                new_name = filename.replace('0_', '', 1)
                os.rename(filename, new_name)