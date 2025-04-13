import seaborn  as sns
import matplotlib.pyplot as plt
# #### Sample data(using x, and y values directly)
categories=['Furniture','Office Supplies','Technology']
profit=[4390.45,3450.50,12340.80]
sales=[80000,23000,90000]
####set the style
sns.set(style="whitegrid")  ### This sets the style of the plot to a white background with gridlines
####'darkgrid','whitegrid','dark','white','ticks'


# #######We imported Matplotlib (import matplotlib.pyplot as plt) even though we are using Seaborn because:
# #######1. Seaborn is Built on Matplotlib
# #######Seaborn is a high-level visualization library that simplifies plotting.
# #######However, it relies on Matplotlib for rendering and customization.
# ########When you call sns.lineplot(), it internally uses Matplotlib to create the plot.


# ####1. Line Plot-Sales over Categories
# plt.figure(figsize=(8,5)) #is used to create a new figure with a specified size for the plot.
# # ###Why Use plt.figure(figsize=(8,5))?
# ####Prevents Overlapping or Distorted Plots
# ####If you create multiple plots in the same script, setting the figure size ensures consistency.Without plt.figure(), the plot may inherit the size of a previous figure.*/

# sns.lineplot(x=categories,y=sales)
# ###sns.lineplot(x='categories',y='sales')### we cannot use this here
# plt.xlabel("categories")
# plt.ylabel("sales")
# plt.title('Sales Trend Over Categories')
# plt.show()  ###this show() is available on matplotlib only , not in seaborn



# ###2.Bar Plot -Profit by Category
# plt.figure(figsize=(8,5))
# barplot=sns.barplot(x=categories,y=profit,errorbar=None)
# # ###barplot is used to capture the output of the bar plot function. 
# # ###While the bar plot will be automatically shown when using sns.barplot(), 
# # ###assigning it to a variable like barplot can be helpful for further customization and adjustments to the plot after it's created.
# plt.title("Average Profit by Category")

# # #########Add labels on top of bars
# for i,value in enumerate(profit):
#     barplot.text(i,value+100,f'{value:.2f}',ha='center')
# plt.show()


# ##### 3. Scatter Plot -Sales vs Profit
# plt.figure(figsize=(8,5))
# sns.scatterplot(x=sales,y=profit)
# plt.title('Sales vs Profit')
# plt.show()

# ###### 4.Heatmap - Correlaation Between Sales and Profit
# import  numpy as np
# import pandas as pd
# data=pd.DataFrame({'Sales':sales,'Profit':profit})
# plt.figure(figsize=(6,4))
# corr=data.corr()
# sns.heatmap(corr,annot=True,cmap='coolwarm',fmt='.2f',linewidths=0.5)
# ####annot=True → Displays the correlation values inside the heatmap.
# ########cmap='coolwarm' → Uses the "coolwarm" color map (blue = negative correlation, red = positive correlation)
# #######fmt='.2f' → Displays numbers with 2 decimal places.
# #######linewidths=0.5 → Adds thin lines between cells for clarity.
# plt.title("Correlation Heatmap")
# plt.show() ## the diagnol of the figure is 1 i.e 100 % correlation






