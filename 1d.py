import pandas as pd
import numpy as np
import os, sys
from pathlib import Path
import traceback
from pprint import pprint

from pandas.core.frame import DataFrame

folderpath = r".\csv_files" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]



# line_count = 0


# print(type(path))
company_set = set()
for file in filepaths:
    data = []
    with open(file, 'r') as infile:
        # print(infile)
        
        df = pd.read_csv(infile, delimiter = ',', skiprows=2, skipfooter=17, engine='python')
        i=1
        for i in df.count():
            val = df.iloc[:,[1,6]]
           
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
dict_weight = {}

for company_name in company_set:
    dict_final['company'] = company_name
    dict_final['weightage'] = list_weight
    # dict = {company: company_name, weightage: []}
    list_final.append(dict_final)
            

for file in filepaths:
    try:
    # print(file)
        with open(file, 'r') as infile:
            df = pd.read_csv(infile, delimiter = ',', skiprows=2, skipfooter=17, engine='python')
            
            for i in df.count():
                val = df.iloc[:,[1,6]]
            
            data = val.values
            
            for row in data:
                company_name = row[0]
                weight = row[1]
                
                month = (file.split('\\')[-1])[0:5]
                # pprint(weight+"    "+month)
                dict_weight = {month:weight}
                # print(month)
                index = 0
                # i = 0
                # pprint(list_final)
                for i, item in enumerate(list_final):
                    if item["company"] == company_name:
                        # print("matched")
                        index = i
                        # print(i)
                        break
                # print(index)
                    # pprint(item) 
                # pprint(company_name)
                # index = i, for i, item in enumerate(list_final) if item["company"] == company_name
                # for item in list_final:
                #     if
                
                # dict_weight[month] = weight
                # print("processing_1")
                pprint(dict_weight)
                # list_weight.append(dict_weight)
                # temp_dict = list_final[index]
                # # print("processing_2")
                # temp_dict['weightage'].append(dict_weight)
                # # print("processing_3")
                # list_final[index] = temp_dict
                # list_final[index]["weightage"].append(dict_weight)
        # print(file)
            
        
    except Exception as err:
        # traceback.print_tb(err.__traceback__)
        # print("error in file path " + path)
        continue
# print("success")
# pprint(list_final)
    df4 = pd.json_normalize(list_final, meta=['company'], record_path=['weightage'])
# print(df4)
            

