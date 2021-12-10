import pandas as pd

list = [{"company": "ACC", "weightage":[{"apr14":"0.1", "apr15":"0.4"}]},

        {"company": "HCL", "weightage":[{"may14":"0.7", "apr15":"0.4"}]}
        
        ]

df = pd.json_normalize(list, record_path=['weightage'], meta=['company'])

print(df)