import pandas as pd
import os

# create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# add an new row
new_row_loc={'Name':'marco','Age':50,'City':'India'}
df.loc[len(df.index)]=new_row_loc

# add one more new row
new_row={'Name':'Suhel','Age':20,'City':'Hidden Leaf'}
df.loc[len(df.index)]=new_row

# create the directory if it doesn't exist
data_dir="data"
os.makedirs(data_dir,exist_ok=True)

# define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

# save the DataFrame to a CSV file
# csv_file_path = 'sample_data.csv'
df.to_csv(file_path, index=False) 

print(f"csv file saved to {file_path}")