import os, zipfile
from zipfile import ZipFile, ZipInfo
import traceback

folder = r'C:\Users\Anshika\Desktop\internships\freelancing\beta\file'
extension = ".zip"
os.chdir(folder)
dir_list = {}

for item in os.listdir(folder): # loop through items in dir
    try:
        # file_name = folder + "/" + item
        with ZipInfo(item, 'r') as zip:
            dir_list = zip.printdir()
            info = zip.getinfo
            # info = ZipInfo.zip
            ZipInfo.is_dir(True)
            # print(zip.read)
            # print(dir_list)
            # print('Extracting all the files now...')
            # zip.extractall()
        
        print('Done!')
        # if item.endswith(extension): # check for ".zip" extension
        #     file_name = os.path.abspath(item) # get full path of files
        #     zip_ref = zipfile.ZipFile(file_name, "r") # create zipfile object
        #     zip_ref.extractall(folder) # extract file to dir
        #     zip_ref.close() # close file
    except Exception as err:
        # traceback.print_tb(err.__traceback__)
        print("error in " + item)
        continue

# with zipfile.ZipFile('july21.zip', "r" ) as z:
    # z.extractall("C:\\Users\\Anshika\\Desktop\\internships\\freelancing\\beta\\files\\")
# for item in os.listdir(folder):
    # if item.endswith(extension):
        # zipfile.ZipFile.extract(item, member= item)