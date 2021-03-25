import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('C:\\Stories\\Fantasy\\archive.zip', 'w')
 
for folder, subfolders, files in os.walk('C:\\Stories\\Fantasy'):
 
    for file in files:
        if file.endswith('.pdf'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()
