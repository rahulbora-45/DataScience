'''Case Study Questions on Rainfall Data Analysis (1901-2015)
Scenario:
You are a climate data analyst working with the "Rainfall in India (1901-2015)" dataset. Your objective is to analyze historical rainfall trends, detect missing data issues, and understand seasonal variations in different regions of India. Your insights will help in climate change assessment, agriculture planning, and disaster management.
Use:  "Rainfall in India (1901-2015)" dataset:
1.How many missing values are present in each column of the dataset?
2.What percentage of data is missing in each year or region?
3.What is the impact of dropping missing values on the dataset?
4.What is the mean, median, and standard deviation of annual rainfall across all years?
5.Which region/state has received the highest and lowest average annual rainfall over the years?
6.What is the yearly trend in average rainfall? Has it increased or decreased over time?
7.What is the total amount of rainfall recorded in India over the dataset period (1901-2015)?
8.How does rainfall vary seasonally (e.g., monsoon, winter, summer, post-monsoon)?
9.Which month records the highest and lowest average rainfall in India?
10.Are there any regions that experience extreme seasonal variations in rainfall?
11.How does filling missing values with different methods (mean, median, forward fill, backward fill) affect the dataset's overall trends?'''

import pandas as pd
df=pd.read_csv("rainfallInIndia.csv")
print(df)
# # 1.How many missing values are present in each column of the dataset?
# print("Total no of empty values:",df.isnull().sum())
# # 2.What percentage of data is missing in each year or region?
# print("Percentage of  data is missing in each region or year:",df.isnull().mean()*100)
# # 3.What is the impact of dropping missing values on the dataset?
# print(df.dropna())
# # 4.What is the mean, median, and standard deviation of annual rainfall across all years?
# print(" region/state has received the highest and lowest average annual rainfall over the years")
# print(df['Annual'].mean())
# print(df['Annual'].median())
# print(df['Annual'].std())
# # 5.Which region/state has received the highest and lowest average annual rainfall over the years?
# print("region/state has received the highest and lowest average annual rainfall over the years")
# print(df['Annual'].min())
# print(df['Annual'].max())

# 6.What is the yearly trend in average rainfall? Has it increased or decreased over time?
print("the yearly trend in average rainfall? Has it increased or decreased over time")
avg=df['Annual'].mean()
if(avg>=0):
    print("increased")
else:
    print("decreased")

# 7.What is the total amount of rainfall recorded in India over the dataset period (1901-2015)?
print("the total amount of rainfall recorded in India over the dataset period (1901-2015)")





# # 8.How does rainfall vary seasonally (e.g., monsoon, winter, summer, post-monsoon)?
# print(" rainfall vary seasonally (e.g., monsoon, winter, summer, post-monsoon)")
# print(df['Jan-Feb'].mean())
# print(df['Mar-May'].mean())
# print(df['Jun-Sep'].mean())
# print(df['Oct-Dec'].mean())

# 9.Which month records the highest and lowest average rainfall in India?

