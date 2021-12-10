import shutil
import os, sys

curr_dir = os.getcwd()
src_dir = curr_dir+'\extracted'
# print(src_dir)
# dest_dir = os.mkdir('csv_files')
os.listdir()

dest_dir = r'.\csv_files'
# print(dest_dir)


for root, dirs, files in os.walk((os.path.normpath(src_dir)), topdown=False):
    # print(root)
    f = root.split("\\")[-1]
    f1 = f.split('_')[-1]
    f2 = f1[0:5]
    for name in files:
        # print(name)
        if name.endswith('.csv'):
            renamed = os.rename(os.path.join(name, files))
            print ("Found")
            SourceFolder = os.path.join(root,renamed)
            
            shutil.copy2(SourceFolder, dest_dir) #copies csv to new folder