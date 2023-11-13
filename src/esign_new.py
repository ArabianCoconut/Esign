import os
import time
import img2pdf
from PIL import Image
from pdf2jpg import pdf2jpg

def esign():
    """
    This function signs all PDF files in the 'PDF_Here' directory using a signature image and saves the signed PDFs in the 'PDF_Signed' directory.
    """
    for filename in os.listdir('PDF_Here'):
        settings = {
                "dir_path": os.path.join('PDF_Here', filename),
                "output": pdf2jpg.convert_pdf2jpg(settings['dir_path'], outputpath='PDF_Signed', pages='ALL'),
                "background": Image.open(settings['output'][0]['output_jpgfiles'][0]),
                "image_open": Image.open('./signature.png').convert('RGBA'),
                "layer": settings['image_open'].resize((800, 800)),
                "x":450,
                "y":2100
        }
    settings['background'].paste(settings['layer'], (settings['x'], settings['y']), settings['layer'])