import pandas as pd
import requests, zipfile, io
import urllib3
import os
from io import BytesIO
from zipfile import ZipFile
import traceback
from gazpacho import Soup

# from urllib.request import urlopen

# initiating a dataframe

full_df = pd.DataFrame()

i = 11
j = 0
# n = 2021
links= []
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
for i in range(12,22):
    
    for j in months:
        url = "https://www1.nseindia.com/content/indices/mcwb_"+str(j)+str(i)+".zip"
        try:
            # print("hi")
            # print(url)
            r = requests.get(url, stream=True)
 
            filename = url.split('/')[-1] # this will take only -1 splitted part of the url
            
            with open("./beta/file/"+filename,'wb') as output_file:
                output_file.write(r.content)
 
        except Exception as err:
            traceback.print_tb(err.__traceback__)
            continue
            
    i=+1


print('Download Completed!!!')
