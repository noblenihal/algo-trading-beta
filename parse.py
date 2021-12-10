from tika import parser
import os, sys
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo
import traceback
# import nltk

folderpath = r".\file" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

count = 0
for path in filepaths:
    try:
        # print(path)
        with ZipFile(path, 'r') as zipObj:
#    # Extract all the contents of zip file in current directory
            listOfFileNames = zipObj.namelist()
            for fileName in listOfFileNames:
       
                if re.search(r"(^nifty50)|(^niftymcwb)|([A-Za-z0-9]\/nifty50)|([A-Za-z0-9]\/niftymcwb)", fileName, flags=re.IGNORECASE):
                    # print(fileName)
                
                    if r"/" in fileName :
                        zipObj.extract(fileName, 'extracted')
                        # print("hi")
                    else:
                        final_path = path.split('\\')[-1]
                        # print(final_path)
                        
                        zipObj.extract(fileName, 'extracted\\'+ final_path)
                    
                # count+=1
            
            else:
                continue
        
    except Exception as err:
        # traceback.print_tb(err.__traceback__)
        # print("error in file path " + path)
        continue
