# Author: Arabian Coconut
# Date Created: 19/08/2023
# Version: 1.0
import os
import time

from modules.esign import e_sign, post_processing, user_input_process

os.makedirs("PDF_Here", exist_ok=True)

print(
        "Please place the PDF files in the PDF_Here directory.\n"
        "Place signature.png in the same directory as this exe.\n"
        "Note: Signature should be in png format with transparent background "
        "and should be named as signature.png\n"
    )
user_input = input("Press enter to continue.")

if user_input == '':
    print("Signing PDF files.\n")
    e_sign()
    print("Signing completed.\n"
          "Please wait while the program processes the files.\n")
    time.sleep(2)
    post_processing()
    print("\nProcessing completed.\n")
    user_input_process()
else:
    print("Error: Something went wrong.\n")
