# Author: Arabian Coconut
# Date Created: 19/08/2023
# Version: 1.0.0
import os

import img2pdf
from PIL import Image
from pdf2jpg import pdf2jpg


def e_sign():
    for filename in os.listdir('PDF_Here'):
        if filename.endswith('.pdf'):
            dir_path = os.path.join('PDF_Here', filename)
            output = pdf2jpg.convert_pdf2jpg(dir_path, outputpath='PDF_Signed', pages='ALL')
            print(f'output: {output}')
            background = Image.open(output[0]['output_jpgfiles'][0])
            layer = Image.open('./signature.png').convert('RGBA')
            layer = layer.resize((800, 800))
            x, y = 450, 2100
            background.paste(layer, (x, y), layer)
            background.save(output[0]['output_jpgfiles'][0])
        else:
            print("Error:No PDF files found."
                  "Please place the PDF files in the same directory as this exe.\n")
            exit()


def post_processing():
    for dirname in os.listdir('PDF_Signed'):
        # Check if the directory name ends with '_dir'
        if dirname.endswith('_dir'):
            # Construct the full path of the directory
            dir_path = os.path.join('PDF_Signed', dirname)
            print(f'Processing {dir_path}...')
            # Loop through all files in the directory
            for filename in os.listdir(dir_path):
                print(f'Processing {filename}...')
                post_processing2(filename, dir_path)


def post_processing2(filename, dir_path):
    if '.pdf.jpg' in filename:
        # Generate a new file name by replacing '.pdf.jpg' with '.jpg'
        new_filename = filename.replace('.pdf.jpg', '.jpg')
        # Rename the file
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
        # Convert the image to PDF
        with open(os.path.join(dir_path, new_filename.replace('.jpg', '.pdf')), 'wb') as f:
            f.write(img2pdf.convert(os.path.join(dir_path, new_filename)))
        # Delete the image file
        os.remove(os.path.join(dir_path, new_filename))
        post_processing3(dir_path)  # continue to post_processing2


def post_processing3(dir_path):
    for filename in os.listdir(dir_path):
        if "0_" in filename:
            print("found.. Removing 0_")
            new_filename = filename.replace('0_', '')
            os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))
        else:
            print("No 0_ containing file found.")


def user_input_process():
    while True:
        user_input = input("Program completed. Do you want to exit? (y/n):").lower()
        if user_input == 'y':
            exit()
        elif user_input == 'n':
            print("Restarting the program. please wait")
            os.system('start sign.exe')


