# E-signing 
### Author: Arabian Coconut
### Date: 19/08/2023
### Version: 1.0.0

---

## Description
This is a simple e-signing application that allows users to sign documents offline using signature images.

---

## How to use
1. Clone the repository
2. ```pip install -r requirements.txt``` to install dependencies
3. ```python sign.py``` to run the application

**Note**: you may use the sign.exe file to run the application without installing python.

---

## Build using pyinstaller
1. ```pip install pyinstaller```
2. ```python pyinstaller --onefile  --add-binary  "D:/Programming/Playground/Python/.venv/Lib/site-packages/pdf2jpg/pdf2jpg.jar;./pdf2jpg/" sign.py```
3. ```commandline start dist/sign.exe```