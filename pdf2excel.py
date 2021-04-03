import os
import subprocess
import sys
import camelot

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir + '/pdf_to_excel.py: Start')

if len(sys.argv) > 1:
    start_dir = sys.argv[1]
else:
    # we will process the current directory
    start_dir = '.'

for dir_name, subdirs, file_list in os.walk(start_dir):    
    os.chdir(dir_name)
    for filename in file_list:
        file_ext = os.path.splitext(filename)[1]
        if file_ext == '.pdf':
            full_path = dir_name + '/' + filename
            # let's try to find some text into the PDF
            print("attempting to OCR: " + full_path)
            # add --deskew only if we are sure that the images might need it
            # because it might create large file together with the option --optmize 0
            cmd = ["ocrmypdf",  "--skip-text --deskew --rotate-pages --clean --optimize 0", '"' + filename + '"', '"' + os.path.splitext(filename)[0] + "-OCR.pdf""]
           
            # you should run OCRmyPDF as a command line tool
            # see https://ocrmypdf.readthedocs.io/en/latest/batch.html#api
            proc = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = proc.stdout

            if proc.returncode == 0:
                print("OCR complete")
            elif proc.returncode == 6:
                print("The file already contains text")
            else:
                print("Error")
