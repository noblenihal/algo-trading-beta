import pandas as pd
import numpy as np
import os, sys
from pathlib import Path
import traceback

from pandas.core.frame import DataFrame

folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

for path in filepaths:
    try:
        f = path.split('_')[-1]
        csvpath= [os.path.join(path, name) for name in os.listdir(path)]
        line_count = 0
        data = []
        # print(type(path))
        for file in csvpath:
            
            with open(file, 'r') as infile:
                # print(infile)
    
                df = pd.read_csv(infile, delimiter = ',', skiprows=2, skipfooter=17, engine='python')
                i=1
                for i in df.count():
                    val = df.iloc[:,[1,6]]
                    # company = df.iloc[:]
                # print(values)
                length = len(val)
                data = val.values
                # print(data)
                company = []
                for i in range(len(data)):
                    company.append(data[i][0])

                weightage = []
                for i in range(len(data)):
                    weightage.append(data[i][1]) 

                dic_weight = {}
                list_weight = []
                dic_final = {}
                list_final = []
                
                for i in data:
                    
                    # print(i[0])
                    if i[0] in dic_final.values():
                        # print(i[0])
                        for j in dic_final.values() :
                            dic_weight[f] = i[1]
                        print(dic_weight)
                        # dic_final[dic_weight]


                    
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        continue