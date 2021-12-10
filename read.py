# import pandas as pd
import csv
# from tika import parser
# import xlrd
import os, sys
from pathlib import Path
import traceback

folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

for path in filepaths:
    try:
        csvpath= [os.path.join(path, name) for name in os.listdir(path)]
        # print(type(path))
        for file in csvpath:

            with open(file, 'r') as f:
                print(f)
                # for line in f.readlines():
                    # array = line.split(',')
                    # first_item = array[0]

                # num_columns = len(array)
                # f.seek(0)
                

                csv_reader = csv.DictReader(f)
                # include_cols = [1,3,5,6,7,8]
                include_cols = [1,6]
                
                for line in csv_reader:
                    print(line[1])
                # for line in csv_reader:
                
                    # content = list(line[i] for i in include_cols)
                    # print(content)    

                # with open('all_beta.csv', 'w') as beta:
                #     fieldnames = ['Security Symbol\Monts', 'Weightage (%)']
                #     csv_writer = csv.DictWriter(beta, fieldnames=fieldnames)
                #     # fieldnames.next()
                #     for line in csv_reader:
                #         field = f"{line['Security Symbol']} {line['Weightage (%)']}"
                #         # del line['Sr. No','']
                #         print(field)
                        # content = list(line[i] for i in include_cols)
                        # print(type(content))
                        # print(content)
                    # print("...................")
                        # csv_writer.writerow(line)
                        # csv_writer.writerows(content)


                # header = next(csv_reader)
            # df = pd.read_excel(file, sheet_name=None)
                # print(header)
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        continue