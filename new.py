import pandas as pd
import os

company_set = {}

##################
folderpath = r".\extracted" 
filepaths  = [os.path.join(folderpath, name) for name in os.listdir(folderpath)]

files = "list of files"

for file in files:
    for company_name in file:
        company_set.app(company_name)


dict_final = {company: "", weightage: []}
list_final = [dict_final]

for company_name in company_set:
    dict = {company: comapany_name, weightage: []}
    list_final.append(dict)

# print(list_final)
# [
#     { company: "acc", weightage: [] },
#     { company: "ambuja", weightage: [] },
#     ...
#     ...
#     { company: "oyo", weightage: [] },
# ]

for file in files:
    for row in file:
        # I'm assuming
        company_name = row[0]
        weightage = row[1]

        ##### Below line is wrong syntax ############
        month = file.file_name

        # get the index of dict to modify it later
        index = next( i for i, item in enumerate(list_final) if item["company"] == company_name )

        # Append weightage
        list_final[index]["weightage"].append({month: weightage})