import pandas as pd
import numpy as np
import os, sys
from pathlib import Path
import traceback

from pandas.core.frame import DataFrame

folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]
dic_weight = {}

dic_final = {}
list_final = []

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
                list_weight = []
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
                # print(weightage)

                
                # f = 'apr12'
                for i in range(0,len(data)):
                    


                    if data[i][0] not in dic_final.values():
                        # print("hii")
                        dic_final['company'] = data[i][0]
                        dic_weight[f] = data[i][1]
                    
                    
                    else:
                        
                        dic_weight[f] = data[i][0]

                    # dic_weight[f] = weightage[i] 
                    # print(weightage, f)
                    # print(dic_final.values())    
                    # if dic_weight not in list_weight:
                    list_weight.append(dic_weight)

                    dic_final['weightage'] = list_weight
                    print(list_weight)
                    # for parse in dic_final:
                    # list_final.append(dic_final.copy())
                    
                    
                    # print(list_final)
            # print("")
        df4 = pd.json_normalize(list_final, meta=['company'], record_path=['weightage'])
        # print(df4)


                #     # company['row[0]']  
                    # print(list)
                # for i in length:
                    # print(values.loc[:,'A'])
                # print(company)
                # print(row[0])
                # print("...next..........")
                # for line in values:
                    # print(line)
                # print((values))
                # print(".............")
                # include_cols = [1,6]
                # print(reader)
                # with open('weightage.csv', 'a', newline='') as outfile:
                #     writer = csv.writer(outfile, delimiter = ',')
                #     if line_count == 0:
                #         writer.writerow(["Symbol\Weightage",values])
                #         line_count +=  1
                #     next(reader, None)
                #     next(reader, None)
                #     next(reader, None)
                #     for row in reader:
                #         # print(type(row))
                #         writer.writerow(row[i] for i in include_cols)
                        # print(row[1])
                    
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        continue