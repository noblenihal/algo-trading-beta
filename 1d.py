import pandas as pd
import numpy as np
import os, sys
from pathlib import Path
import traceback
from pprint import pprint

from pandas.core.frame import DataFrame

folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]


for path in filepaths:
    try:
        # f = path.split('_')[-1]
        
        csvpath= [os.path.join(path, name) for name in os.listdir(path)]
        line_count = 0
        data = []
        
        # print(type(path))
        company_set = set()
        for file in csvpath:
            
            with open(file, 'r') as infile:
                # print(infile)
                
                df = pd.read_csv(infile, delimiter = ',', skiprows=2, skipfooter=17, engine='python')
                i=1
                for i in df.count():
                    val = df.iloc[:,[1,6]]
                    # company = df.iloc[:]
                # print(values)
                # length = len(val)
                data = val.values
                # print(data)
                company = []
                for i in range(len(data)):
                    company.append(data[i][0])

                weightage = []
                for i in range(len(data)):
                    weightage.append(data[i][1]) 
                # print(weightage)

                for company_name in company:
                    company_set.add(company_name)
                
        
                # dict_final = {company: "", weightage: []}
                # list_final = []

        dict_final = {}
        list_final = []
        list_weight = []

        for company_name in company_set:
            dict_final['company'] = company_name
            dict_final['weightage'] = list_weight
            # dict = {company: company_name, weightage: []}
            list_final.append(dict_final.copy())
                   
        for file in csvpath:
            # print(file)
            f = file.split("\\")[-2]
            f1 = f.split('_')[-1]
            f2 = f1[0:5]
            
            with open(file, 'r') as infile:
                df = pd.read_csv(infile, delimiter = ',', skiprows=2, skipfooter=17, engine='python')
                
                for i in df.count():
                    val = df.iloc[:,[1,6]]
                
                data = val.values
                
                for row in data:
                    company_name = row[0]
                    weightage = row[1]

                   
                    
                    
                    index = next( i for i, item in enumerate(list_final) if item["company"] == company_name )

                    list_final[index]["weightage"].append({f2: weightage})
            # print(f2)
                    # pprint(row)
                # for i in range(len(data)):
                #     # company_set.app(company[i])
                #     if company[i] not in dic_final.values():
                #         dic_final['company'] = company[i]
                #         # list_weight.append(dic_weight)
                #         dic_final['weightage'] = list_weight
                #     list_final.append(dic_final.copy())
              
        pprint(list_final)
        # print("\t")
        
                    
                    # print(list_final)
            # print("")
        df4 = pd.json_normalize(list_final, meta=['company'], record_path=['weightage'])
        # print(df4)
                    
    except Exception as err:
        traceback.print_tb(err.__traceback__)
        continue
    # print(company_set)
# pprint(list_final) 
    # pprint(len(list_final))



# check file name...why is it repeating.