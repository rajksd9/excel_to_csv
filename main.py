import pandas as pd
import os

input_file = input("Enter the file path")
df=pd.read_excel(input_file)

# to get the sheet names
xls= pd.ExcelFile(input_file)
print(xls.sheet_names)


#creating a directory if not already exist 
dir_name= input_file.split(".xlsx")[0]

if (not os.path.exists(dir_name)):
    os.mkdir(dir_name)


#creating and adding csv files
for item in xls.sheet_names:
    df=pd.read_excel(input_file,sheet_name=item)
    df.to_csv(f"{dir_name}/{item}.csv",index=False)
    print(item+"\n")
    print(df)
