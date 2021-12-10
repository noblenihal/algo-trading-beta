# # # from io import BytesIO
# # # from zipfile import ZipFile
# # # from urllib.request import urlopen
# # # # or: requests.get(url).content

# # # resp = urlopen("https://www.niftyindices.com/Market_Capitalisation_Weightage_Beta_for_NIFTY_50_And_NIFTY_Next_50/mcwb_jul21.zip")
# # # zipfile = ZipFile(BytesIO(resp.read()))
# # # zipfile.namelist()
# # # # for line in zipfile.open(file).readlines():
# # # #     print(line.decode('utf-8'))

# import requests
# import io
# import zipfile

# def download_extract_zip(url):
#     """
#     Download a ZIP file and extract its contents in memory
#     yields (filename, file-like object) pairs
#     """
#     response = requests.get("https://www.niftyindices.com/Market_Capitalisation_Weightage_Beta_for_NIFTY_50_And_NIFTY_Next_50/mcwb_jul21.zip")
    # with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
    #     for zipinfo in thezip.infolist():
    #         with thezip.open(zipinfo) as thefile:
    #             yield zipinfo.filename, thefile

# print("hi")

import urllib3
import zipfile
import urllib.request
data = urllib.request.urlretrieve("https://www.niftyindices.com/Market_Capitalisation_Weightage_Beta_for_NIFTY_50_And_NIFTY_Next_50/mcwb_jul21.zip", "jul21.zip")

# urllib.urlretrieve("https://www.niftyindices.com/Market_Capitalisation_Weightage_Beta_for_NIFTY_50_And_NIFTY_Next_50/mcwb_jul21.zip", "july21.zip")
with zipfile.ZipFile('july21.zip', "r" ) as z:
    z.extractall("C:\\Users\\Anshika\\Desktop\\internships\\freelancing\\beta\\files\\")

print("extracted!!")