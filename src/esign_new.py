import glob
import os
import time
import img2pdf
from PIL import Image
from pdf2jpg import pdf2jpg

PDF_HERE_DIR = 'src/PDF_Here'
PDF_SIGNED_DIR = 'src/PDF_Signed'
SIGNATURE_PATH = 'src/signature.png'
SIGNATURE_SIZE = (800, 800)
SIGNATURE_POSITION = (450, 2100)

def log():
    with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(
                "Error: No PDF files found.\n"
                f"Please place the PDF files in the '{PDF_HERE_DIR}' directory.\n"
                "Also, make sure the signature image is in the same directory as this exe and with transparent background.\n"
            )
    time.sleep(5)
    exit(0)

def create_folders():
    """
    This function creates the 'PDF_Here' and 'PDF_Signed' directories if they don't exist.
    """
    try:
        os.mkdir(PDF_HERE_DIR)
        os.mkdir(PDF_SIGNED_DIR)
    except FileExistsError:
        with open('log_warning.txt', 'w', encoding='utf-8') as f:
            f.write(
                "Warning: The 'PDF_Here' and 'PDF_Signed' directories already exist.\n"
                "Please delete them and run the program again. If the program do not work correctly.\n"
            )

def esign():
    """
    This function signs all PDF files in the 'PDF_Here' directory using a signature image and saves the signed PDFs in the 'PDF_Signed' directory.
    """
    try:
        create_folders()
        # Get the paths of all PDF files in the 'PDF_Here' directory
        pdf_paths = glob.glob(f'{PDF_HERE_DIR}/*.pdf')
        print(f'pdf_paths: {pdf_paths}') #* Debug

        for pdf_path in pdf_paths:
            # Convert the PDF to JPG
            jpg_path = pdf2jpg.convert_pdf2jpg(pdf_path, outputpath=PDF_SIGNED_DIR, pages='ALL')

            # Open the JPG as a PIL Image
            background = Image.open(jpg_path)

            # Open the signature image and resize it
            signature = Image.open(SIGNATURE_PATH).convert('RGBA')
            signature_resized = signature.resize(SIGNATURE_SIZE)

            # Paste the signature onto the background
            background.paste(signature_resized, SIGNATURE_POSITION, signature_resized)

            # Save the signed PDF
            background.save(jpg_path, format='png', quality=100)

    except FileNotFoundError:
        log()
        
def convert_jpg_to_pdf(): #! This function is not working properly
    jpg_paths=glob.glob(f'{PDF_SIGNED_DIR}/*.pdf_dir/*.pdf.jpg')
    # new_name="".join(jpg_paths).replace("0_","").replace(".pdf.jpg",".png")
    # os.renames("".join(jpg_paths),new_name)
    for jpg_path in jpg_paths:
        with open('src\PDF_Signed\Learners_License.pdf_dir\Learners_License.png', "rb") as f:
            img = Image.open(f).convert('RGBA')
            pdf_bytes = img2pdf.convert(img)
        # with open(jpg_path[:-4] + ".pdf", "wb") as f:
        #     f.write(pdf_bytes)

# esign()
convert_jpg_to_pdf()