import pandas as pd
import os

#create a sample data frame

data= {"Name":["Alice", "Charlie", "Bob"],
       "Age": [25, 30, 35], 
       "city":["New York", "Los Angles", "Chichago"]}
       
df= pd.DataFrame(data)

# Adding new row to data

new_row_loc= {"Name":"gf1", "Age": 20, "city":"city1"}

df.loc[len(df.index)]=new_row_loc

#Ensure that data directory exist at root level

data_dir= "Data"
os.makedirs(data_dir,exist_ok=True)

#Define the file path

file_path= os.path.join(data_dir,"sample_data.csv")

#save the data frame to csv

df.to_csv(file_path,index=False)
print("csv file saved to ", file_path)