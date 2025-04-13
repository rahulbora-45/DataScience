#Silce Row
import pandas as pd
df=pd.read_csv('rahul.csv')
df['sum']=df['total_bill']+df['tip'] # creatinga new column in the dataframe by adding the value of total_bill and tip


# print("-------------------------------------------")
# #Load the CSV file
# df=pd.read_csv('rahul.csv')
# ##1.Read CSV
# print("Data Load Successfully!\n")
# # #2.Display first 10 rows
print("First 10 rows:\n",df.head(),"\n")
# # #3.Display last 5 rows
# print(df)
# print("Last 5 rows:\n",df.tail(),"\n")


# #4.DataFrame  summary
# print("DataFrame Info:\n")
# df.info()
# # #5.Descriptive statisticS
# print("Descriptive Statistics:\n",df.describe(),"\n")
# #6.Shape of DataFrame
# print("Descriptibe DataFrame:\n",df.shape,"\n")
# #7.COlumn names
# print("Column Names: \n",df.columns,"\n")
# #8.Checking for missing values
# print("Missing Values:\n",df.isnull().sum(),"\n")

# # # 9.Drop rows with missing values
# df_cleaned=df.dropna()  ##it will remove the row containing Nan value
# print("Data after dropping missing values: \n",df_cleaned.head(),"\n")
# # 10.Fill missing values with 0
# df_filled= df.fillna(0) ##it will fill the postion which contains Nan with 0
# print("Data after filling missing values:\n",df_filled.head(),"\n")

# # #11.Group by a  column and aggregrate
# grouped_data=df.groupby('day')['total_bill'].sum()
# ##12 Sort values by total_bill in descending oder
# sorted_df=df.sort_values(by='total_bill',ascending=False)
# print("Top 5 Total Records:\n",sorted_df.head(),"\n")


# ####-----------------------------------------------------------------
# ##13.Aply function to transform total_bill 
# ### .apply(): The .apply() function is used to apply a function along a particular axis of the DataFrame (in this case, a column). 
# ###It can be used with both functions and lambda functions (anonymous functions).

# df['total_bill_in_hundreds']=df['total_bill'].apply(lambda x:x/100)

# ###df[['total_bill', 'total_bill_in_hundreds']]: This selects two columns, total_bill and total_bill_in_hundreds, 
# # ###from the DataFrame df for display.
# print("Transformed Total Bill Data:\n",df[['total_bill','total_bill_in_hundreds']].head(),"\n")
# ###########--------------------------------------


##### 'inner': An inner join will only include rows where there is a matching value in both DataFrames (df1 and df2).
#####If a row in df1 doesn't have a corresponding row in df2, it will be excluded, and vice versa.
#####Other options for how are:
#####'left': Keep all rows from df1 and only matching rows from df2.
#####'right': Keep all rows from df2 and only matching rows from df1.
#####'outer': Keep all rows from both df1 and df2, filling missing values with NaN where there is no match.


# ##14.Merge operation (Assuming df1 and df2 are available for merging)

# df_merge=df1.merge(df2,on='Customer_ID',how='inner')
# print(df_merge.head())

# ##15.Concatenate (Assuming df1 and df2 exist)
# df_combined=pd.concat([df1,df2],axis=0)
####Note: If the columns in df1 and df2 are not the same, concat() will align them based on their column names, 
# ###and fill any missing columns with NaN.










# ##16.Pivot Table Example
# # ////## we can use this in when we have categorical attribute only otherwise we cannot use    pivotable
# pivot_table=df.pivot_table(values='total_bill',index='day',columns='Gender',aggfunc='sum')
# print("Pivot Table:\n",pivot_table,"\n")
# #17.Accessing a column
# print("Total Bill Column:\n",df['total_bill'].head(),"\n")

# ##18.Filtering using loc
# filtered_df=df.loc[df['total_bill']>20]
# print("Filtered Data (Total Bill>20):\n",filtered_df.head(),"\n")
# ##19.Accessing rows with iloc
# print("First 5 rows using iloc:\n",df.iloc[0:5],"\n")
# ##20 Renaming columns
# #  we have make new variable here becuase we  dont want to make changes in the original data
# df_renamed=df.rename(columns={'total_bill':'Total_Bill_Amount'})
# print("Renamed Column Names:\n",df_renamed.columns,"\n")
