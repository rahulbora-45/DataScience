### if we use single input then it is simple linear regression
## if we have multiple parmeter then   it is multiple linear rregression

#### mmultiple citeria then it is  polynomail linear regression


## first if all we have of calculate the 


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Load dataset
# Load the Sample Superstore dataset
#Load the Sample Superstore dataset
#file_path="D:/sem4/int 375/A154107982_22138_18_2025_Sample - Superstore_Orders"
file_path="D:/sem4/int 375/A154107982_22138_18_2025_Sample - Superstore_Orders/Sample - Superstore_Orders.xlsx"
data=pd.read_excel(file_path,sheet_name='Sample - Superstore_Orders') ## this is applicable if  we are using xlsx i.e excel file because in xlsx file only there will be sheet 
#### In csv file we dont have something like sheet thats why we cannot use the above sheet_name parameter
####'csv- comma seperated value ;;- csv is like text file
#### if we want to define the sheet name in the the read_excel then we introduce another parameter read_excel(" ",sheet=sheet_name)
##### xlsx files aalways represent in terms of sheet 
#/ here we are using read_excel because we are using .xlsx  if .csv then read_csv
# ### we have change "\" ----"/":- becuase we have change it to window to local machine
#Preview the data
print(data.head())
#Set the style
sns.set(style="whitegrid")
#1. Line plot - Sales over Order Date
plt.figure(figsize=(10,5))
data['Order Date']=pd.to_datetime(data['Order Date'])
sns.lineplot(data=data, x='Order Date', y='Sales')
plt.title('Sales Trend Over Time')
plt.show()
#2. bar plot - Average Profit by Category
plt.figure(figsize=(8,5))
barplot=sns.barplot(data=data, x='Category', y='Profit', errorbar=None)
for p in barplot.patches:
    value=f'[p.get_height():.2f]'#Format the value to 2 decimal places
    barplot.annotate(value,(p.get_x()+p.get_width()/2.,p.get_height()),ha='center', va='center',fontsize=10,color='black',xytext=(0,5),textcoords='offset points')

'''barplot.patches iterates through all the bars.
p.get_x() +p.get_width()/2. centers the label on the bar.
p.get_height() sets the value for the label.
xytext=(0,5) offsets the label slightly above the bar for better readability.
annotate() is a Matplotlib function that adds an annotation (text +arrow)
to a specific point in a plot.'''

plt.title('Average Profit by Category')
plt.show()
#3. Scatter Plot - Sales vs Profit, colored by Ship Mode
plt.figure(figsize=(8,5))
sns.scatterplot(data=data, x='Sales', y='Profit', hue='Ship Mode', style='Ship Mode', s=100)
plt.title('Sales vs Profit by Ship Mode')
plt.show()

#4. Heatmap- Correlation Between Numercial Fields
plt.figure(figsize=(6,4))
corr=data[['Sales','Profit','Quantity','Discount']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)

plt.title('Correltion Heatmap')
plt.show()
