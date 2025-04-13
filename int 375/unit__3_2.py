import pandas as pd
import matplotlib.pyplot as plt
#Load dataset

df = pd.read_excel("A154107982_22138_18_2025_Sample - Superstore_Orders/Sample - Superstore_Orders.xlsx")

# ####Here, Order Date and Ship Date are strings (text format), not actual date objects.
# #### So we need to convert it into datetime format
#  #Convert date columns to datetime
# df['Order Date'] = pd.to_datetime(df['Order Date']) #### YYYY-MM-DD
# df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# '''We convert 'Order Date' and 'Ship Date' into datetime format because:
# It allows us to perform date-based operations (like extracting the year, month, or day).
# It enables time-series analysis (e.g., grouping by month, calculating delays).
# It helps with sorting and filtering data chronologically.
# '''

#  #1. Sales Trends Over Time
# #How do total sales vary over different months and years? 

# df['Year-Month'] = df['Order Date'].dt.to_period('M') ###Extracts the Year-Month from the 'Order Date' column.

# ##### .dt -->(Datetime Accessor)
# ##### .to_period()---->This converts the date into a period object representing Year-Month (YYYY-MM).
# #####Converts it into a monthly period format (YYYY-MM).
# '''The reason we use Order Date instead of Ship Date for analyzing sales trends over time is that sales are typically recorded when an order is placed, not when it is shipped.'''


# '''Parameter	Description	Example Output 
# 'Y'	Yearly	2023
# 'M'	Monthly	2023-01
# 'Q'	Quarterly	2023Q1
# 'W'	Weekly	2023-05-14 (Week starting)
# 'D'	Daily	2023-05-14
# 'H'	Hourly	2023-05-14 15:00
# 'T' or 'min'	Minute	2023-05-14 15:30'''
# sales_trend = df.groupby('Year-Month')['Sales'].sum()
# plt.figure(figsize=(12, 6))
# sales_trend.plot(marker='o')####Why Doesn’t sales_trend.plot(marker='o') Need plt ?In this case, sales_trend is a Pandas Series, and Pandas has built-in plotting functionality using Matplotlib.
# plt.title('Total Sales Over Time')
# '''Pandas automatically puts the index (Year-Month) on the X-axis.
# The values (Sales) go on the Y-axis.
# '''
# plt.xlabel('Year-Month')
# plt.ylabel('Total Sales')
# plt.xticks(rotation=45)####This line is used to rotate the labels on the x-axis to improve readability.
# plt.show()
# df.info()




#  #2. Most Profitable Categories
# #Which product categories generate the highest profit?
# plt.figure(figsize=(8, 5))
# category_profit = df.groupby('Category')['Profit'].sum().sort_values()##category_profit is a Pandas Series (df.groupby('Category')['Profit'].sum() creates a Series).
# category_profit.plot(kind='bar', color='skyblue') ## we cannot use bar() here
# plt.title('Total Profit by Category')
# plt.xlabel('Category')
# plt.ylabel('Total Profit')
# plt.show()

# # 3. Regional Performance
# #Which regions contribute the most to sales and profit?
# plt.figure(figsize=(10, 5))
# region_sales = df.groupby('Region')['Sales'].sum().sort_values()
# region_sales.plot(kind='bar', color='lightcoral')
# plt.title('Sales by Region')
# plt.xlabel('Region') ### index always come to x axis
# plt.ylabel('Total Sales')
# plt.show()

# 4. Customer Segments Analysis
#How do different customer segments (Consumer, Home Office, Corporate) contribute to sales and profit?
plt.figure(figsize=(6, 6))
df['Segment'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution by Customer Segment')
plt.ylabel('')
plt.show()

# #5. Impact of Discounts on Profitability
# #How does increasing the discount percentage affect profitability? 
# plt.figure(figsize=(8, 5))
# plt.scatter(df.Discount,df.Profit,color="blue",marker='o')
# ######or#######plt.scatter(df['Discount'],df['Profit'],color="blue",marker='o')
# plt.title('Impact of Discount on Profit')
# plt.xlabel('Discount')
# plt.ylabel('Profit')
# plt.show()


# # ########### horrizontal bar implementation
# # 6. Best and Worst Performing States
# #Which states have the highest and lowest total sales?
# plt.figure(figsize=(12, 6))
# state_sales = df.groupby('State/Province')['Sales'].sum().sort_values()
# state_sales[-10:].plot(kind='barh', color='seagreen')
# plt.title('Top 10 States by Sales')
# plt.xlabel('Total Sales') ## AS i am using horizontal bar so x label becomes totalSales
# plt.ylabel('State')
# plt.show()

# 7. Top Selling Products
#What are the top 10 most sold products in terms of quantity? 
top_products = df.groupby('Product Name')['Quantity'].sum().nlargest(10)
##The nlargest(n) function in Pandas is used to get the top n values from a Series in descending order.
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='orange')
plt.title('Top 10 Selling Products by Quantity')
plt.xlabel('Product Name')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45,ha='right')  ## by default ha=centre
plt.show()

# # 8. Shipping Mode Preferences
# #What are the most commonly used shipping modes, and how do they impact sales and delivery time? 
# plt.figure(figsize=(8, 5))
# df['Ship Mode'].value_counts().plot(kind='bar', color='purple')
# plt.title('Shipping Mode Preferences')
# plt.xlabel('Shipping Mode')
# plt.ylabel('Number of Orders')
# plt.show()

# # # 9. Order Frequency by Customer
# # ##on single column data we use histogram
# #How many customers place multiple orders, and what percentage of orders come from repeat customers?
# customer_orders = df.groupby('Customer Name')['Order ID'].nunique() ##value here is order id and index==Customer Name
# # plt.figure(figsize=(8, 5))
# # customer_orders.hist(bins=20, color='teal', edgecolor='black')
# # plt.title('Order Frequency by Customer')
# # plt.xlabel('Number of Orders')
# # plt.ylabel('Number of Customers')
# # plt.show()

# ### what percentage of orders come from repeat customers?
# repeat_customer=customer_orders[customer_orders>1]
# orders_from_repeat_customers=repeat_customer.sum()
# total_orders=df['Order ID'].nunique()## .nunique():--: This is a Pandas Series method that counts the number of unique values within the Series.
# percentage_orders_from_repeat_customers = (orders_from_repeat_customers / total_orders) * 100
# print(f"Percentage of orders from repeat customers: {percentage_orders_from_repeat_customers:.2f}%")


# ####10. Seasonality in Sales
# ####Are there certain months where sales peak, indicating seasonality?
# df['Month'] = df['Order Date'].dt.month ##.dt.month extracts the month number (1 for January, 2 for February, etc.) from each date.
# monthly_sales = df.groupby('Month')['Sales'].mean()
# plt.figure(figsize=(8, 5))
# monthly_sales.plot(kind='bar', color='darkblue')
# plt.title('Average Monthly Sales')
# plt.xlabel('Month')
# plt.ylabel('Average Sales')
# plt.xticks(rotation=0)
# plt.show()


# df['month']=df['Order Date'].dt.month
# monthly_sales=df.groupby(['month'])['Sales'].mean()
# plt.figure(figsize=(8,5))
# monthly_sales.plot(kind='bar',color='darkblue')
# plt.title("Order date")





