# Author: Arabian Coconut
# Date Created: 19/08/2023
# Date Modified: 03/12/2023
# Version: 1.0.1
import time

from modules.esign import esign, create_folders

INFO_TEXT = "Signing PDF files.\n"
POSITIVE_RESPONSE = "Signing completed.\n + Please wait while the program processes the files.\n"
USER_QUESTION = "Do you want to sign more files? (y/n): "
PROCESSING_TEXT = "\nProcessing completed.\n"

print(
        "Please place the PDF files in the PDF_Here directory.\n"
        "Place signature.png in the same directory as this exe.\n"
        "Note: Signature should be in png format with transparent background "
        "and should be named as signature.png\n"
    )

create_folders()
user_input = input("Press enter to continue...")

while user_input == '': #! This is a temporary Refractor. Will be removed in future versions.
    print(INFO_TEXT)
    esign()
    print(POSITIVE_RESPONSE)
    time.sleep(2)
    print(PROCESSING_TEXT)
    user_input = input(USER_QUESTION)
    if user_input == 'y':
        print(INFO_TEXT)
        esign()
        print(POSITIVE_RESPONSE)
        time.sleep(2)
        print(PROCESSING_TEXT)
        user_input = input(USER_QUESTION)
    else:
        print("Exiting program.")
        break