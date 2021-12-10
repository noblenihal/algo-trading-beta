import csv
import os, sys
from pathlib import Path
import traceback

folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

for path in filepaths:
    try:
        f = path.split('_')[-1]
        values = []
        values.append(f)
        # f1 = f[:-4]
        # print(f)
        csvpath= [os.path.join(path, name) for name in os.listdir(path)]
        line_count = 0
        # print(type(path))
        for file in csvpath:
            # print(file)
            # f = file.split('\\')[-2]
            # print(f)
            # f1 = f[:-4]
            # f2 = f1[5:]
            # print(f2)
            with open(file, 'r') as infile:
                # print(infile)
                reader = csv.reader(infile, delimiter = ',')
                include_cols = [1,6]
                # print(reader)
                with open('weightage.csv', 'a', newline='') as outfile:
                    writer = csv.writer(outfile, delimiter = ',')
                    if line_count == 0:
                        writer.writerow(["Symbol\Weightage",values])
                        line_count +=  1
                    next(reader, None)
                    next(reader, None)
                    next(reader, None)
                    for row in reader:
                        # print(type(row))
                        writer.writerow(row[i] for i in include_cols)
                        # print(row[1])
                    
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        continue