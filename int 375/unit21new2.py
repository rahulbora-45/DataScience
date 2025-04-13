# #whatever function it might be  if it starts with "is" it always return true or false
import pandas as pd
import numpy as np
#creating a dataset eith missing values
data={
   'Id':[1,2,3,4,5],
   'Name':['Alice','Bob',np.nan,'David','Eve'],
   'Age':[25,np.nan,30,np.nan,40],
   'City':['New York','Los Angeles','Chicago',np.nan,'Houston'],
   'Salary':[50000,60000,np.nan,80000,70000] 
}
df=pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

# ###Detecting missing values
# print("\nMissing values in each column: ")
# print(df.isnull().sum())


# ####Dropping rows with missing values
# df_dropped_rows=df.dropna()
# print("\nDataFrame after dropping rows with missing values:")
# print(df_dropped_rows)

# #####Dropping columns with missing values
# df_dropped_cols=df.dropna(axis=1)
# print("\nDataFrame after dropping columns with missing values:")
# print(df_dropped_cols)


# ############--------
# ###Filling missing values with specifis values

# ## 'Age': df['Age'].mean(): For the Age column, any missing values (NaNs) will be replaced with the mean of the Age column. The .mean() function calculates the average of the Age column.
# ###'City': 'Unknown': For the City column, any missing values will be replaced with the string 'Unknown'. This is a constant value, which is useful for categorical or text columns.
# ###'Salary': df['Salary'].median(): For the Salary column, any missing values will be replaced with the median of the Salary column. The .median() function calculates the middle value of the Salary column.
# df_filled=df.fillna({'Age':df['Age'].mean(),'City':'Unknown','Salary':df['Salary'].median()})
# print("\nDataFrame after filling missing values:")
# print(df_filled)
# ###Forward fill(updated to avoid FutureWarning)

# ##### df.ffill(): This applies forward filling to the entire DataFrame df. 
# ##### It fills the missing values with the last available non-null value in each column, propagating forward.
# #####It works row by row, filling the missing values with the previous valid value in the column.
# df_ffill=df.ffill()
# print("\nDataFrame after forward filling")
# print(df_ffill)

# #####_-------------------------------



# ###Interpolating missing values (updated to avoid FutureWarning)

# #########Interpolation: Fills missing values by estimating them based on the existing data points in the column.
# #########By default, it uses linear interpolation, but other interpolation methods can be specified

# df_numeric=df.select_dtypes(include=[np.number])
# ###print(df_numeric)## it will print only numeric values

# #### df.select_dtypes():
# #### select_dtypes() is a function in pandas that allows you to select columns of a DataFrame based on their data type (dtype).
# #### It accepts an argument include which can specify one or more data types. It can also accept exclude to filter out certain data types if needed.
# #### include=[np.number]:
# #### Here, the argument include=[np.number] specifies that you want to select all columns that have numeric data types.

# df_interpolated=df_numeric.interpolate()##by default interpolate() performs linear interpolation
# ######Linear Interpolation: The method works by estimating the missing value based on a linear relationship between the previous and next valid values in the column. 
# ####The result is that the missing values are filled smoothly based on the known data points.

# ##Merge back non-numeric columns
# df_final=df.copy()
# df_final[df_numeric.columns]=df_interpolated
# print(df_final)

# ##############---------------------------------------


import pandas as pd
import numpy as np
data = {
    'ID':[1,2,3,4,5],
    'Name':['Alice','Bob',np.nan, 'David', 'Eve'],
    'Age' : [25, np.nan, 30, np.nan, 40],
    'City' : ['New York', 'Los Angeles', 'Chicago', np.nan, 'Houston'],
    'Salary' : [50000,60000, np.nan, 80000, 70000]
}
# df = pd.DataFrame(data)
# print(df)
# print("Original Data Frame with missing value:")
# print(df.isnull().sum())
# df_dropped_rows = df.dropna()
# print("Data Frame after dropping rows with missing values:")
# print(df_dropped_rows)

# df_dropped_cols = df.dropna(axis=1)
# print("Data Frame after dropping missing values columns:")
# print(df_dropped_cols)

# df_filled = df.fillna({'Age':df['Age'].mean(), 'City':'Unknown', 'Salary': df['Salary'].median()})
# print("Data Frame after filling missing values:")
# print(df_filled)

# df_ffill = df.ffill()
# print("Data Frame after Forward Fill:")
# print(df_ffill)
##### #########------------------------------------------------------------
##### The bfill() function fills missing values (NaNs) in a DataFrame df by propagating the next valid value backward.
##### This means if a row has a missing value, it will be filled with the value from the subsequent row.
##### If the last row has a NaN value, it will remain NaN because there is no subsequent row to fill it with.

# df_bfill = df.bfill()
# print("Data Fra,e after backwad fill:")
# print(df_bfill)
#######_------------------------------------------

# # Interpolate missing values(updated to avoid Future Warning)
# df_numeric = df.select_dtypes(include=[np.number])
# df_interpolated = df_numeric.interpolate()

# # Merge back non-numeric value
# df_final = df.copy()
# df_final[df_numeric.columns] = df_interpolated

# print("\nDataFrame after interpolation:")
# print(df_final)


#saving cleaned data
cleaned_file_path="ABC.CSV"
df.to_csv(cleaned_file_path,index=False)
####df.to_csv(): This is a pandas function used to write a DataFrame to a CSV file.

####cleaned_file_path is the location and name of the CSV file where the data will be saved. 
####In this case, it will save the DataFrame to "ABC.CSV".

####Setting index=False ensures that the index is not written to the CSV file, and only the actual data columns are saved. 
# ###If you set it to True, the index (row numbers) would be included in the CSV file as an extra column.
###
print(f"Cleaned data saved to: {cleaned_file_path}")
###This line prints a confirmation message to the console to let you know that the data has been successfully saved.