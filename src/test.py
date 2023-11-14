import os
import glob

PDF_SIGNED_DIR = 'src/PDF_Signed'


jpg_paths=glob.glob(f'{PDF_SIGNED_DIR}/*.pdf_dir/*.pdf.jpg')
NEW_NAME="".join(jpg_paths).replace("0_","").replace(".pdf.jpg",".png")
os.renames("".join(jpg_paths),NEW_NAME)
