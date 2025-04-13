'''Question: Customer Purchase Behavior Analysis
A retail company collects transaction data from its customers, storing purchase amounts in a 2D NumPy 
array, where each row represents a customer and each column represents daily transactions over a 
month. The company wants to analyze spending patterns.
Problem Statement:
Using NumPy, analyze customer purchase behavior by performing the following tasks:
1. Create a 2D NumPy array to represent purchase amounts.
2. Compute the total spending of each customer over the month.
3. Find the average daily spending per customer.
4. Finds customers who spent more than $3000'''

# import numpy as np
# purchase_amount = np.array([
#     [100, 120, 150, 90, 110],  # Customer 1
#     [200, 210, 180, 3000, 170],  # Customer 2
#     [50, 60, 70, 40, 30]        # Customer 3
# ])
# acc=np.array(purchase_amount)

# print("the total spending of each customer over the month.")
# total_spending=np.sum(acc,axis=1)
# print(total_spending)

# print("the average daily spending per customer.")
# print(np.mean(acc,axis=1))


# print("customers who spent more than $3000")
# customer_over_3000=total_spending>3000
# print(customer_over_3000)
# customer_who_spent_more_than_3000=np.where(customer_over_3000)[0]## Get the indices of customers

# if len(customer_who_spent_more_than_3000)>0:
#     print("Customers who spent more than $3000:",customer_who_spent_more_than_3000+ 1)
# else:
#     print("No customers spent more than $3000.")



# import numpy as np

# stock_prices = np.array([
#     [100, 105, 110, 115, 120],  # Stock 1
#     [200, 210, 205, 215, 225],  # Stock 2
#     [50, 55, 52, 57, 60]        # Stock 3
# ])

# print("Find the maximum and minimum prices for each stock.")
# Maximum=np.max(stock_prices,axis=1)
# print(Maximum)
# Minimum=np.min(stock_prices,axis=1)
# print(Minimum)
# print("Compute the cumulative sum of each stock")
# print(np.cumsum(stock_prices,axis=1)) 

# print("Sort stocks based on average return.")




'''A smart city initiative installs IoT sensors on roads to monitor traffic congestion. The sensor data is stored 
in a 2D NumPy array, where each row represents a different road, and each column represents hourly 
traffic counts.
Problem Statement:
Using NumPy, analyze traffic patterns by performing the following operations:
1. Create a 2D NumPy array to store traffic data.
2. Find the average vehicle count per road over the day.
3. Identify roads with peak congestion periods (highest values).
4. Detect roads with traffic exceeding a critical congestion threshold.
5. Compute the cumulative sum of vehicles passing each road.
6. Identify hourly trends by reshaping data into time blocks (e.g., morning/evening).
7. Simulate future traffic data using NumPy’s random functions.'''


import numpy as np

traffic_data = np.array([
    [30, 50, 70, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100],
    [40, 60, 80, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110],
    [20, 40, 60, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090],
    [50, 70, 90, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120],
    [60, 80, 100, 130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080, 1130]
])


# average=np.mean(traffic_data,axis=1)

# peak_congestion_per_road=np.max(traffic_data,axis=1)


# print("roads with traffic exceeding a critical congestion threshold")
# critical_threshold=700

# data=np.max(traffic_data,axis=1)
# # road_above_threshold=data>700
# print(road_above_threshold)
# print(np.any(traffic_data>critical_threshold,axis=1))


# print("Compute the cumulative sum of vehicles passing each road.")
# print(np.cumsum(traffic_data,axis=1))


# print("Identify hourly trends by reshaping data into time blocks")
# print(f" morning: {np.sum(traffic_data[:,6:13],axis=1)}")
# print(f"evening:{np.sum(traffic_data[:,18:],axis=1)}")

# print("Simulate future traffic data using NumPy’s random functions")
# future_traffic_data = np.random.normal(loc=traffic_data.mean(), scale=100, size=(5, 24))











'''A hospital monitors patient health metrics (heart rate, blood pressure, oxygen levels) using wearable 
devices. The data is stored in a 2D NumPy array, where each row represents a patient and each column 
represents daily health readings.
Problem Statement:
Using NumPy, analyze patient health trends and detect anomalies:
1. Create a 2D NumPy array to represent patient health metrics.
2. Find the mean and standard deviation for each metric.
3. Identify patients with critical readings (above or below thresholds).
4. Sort patients based on average heart rate.
5. Detect patients with anomalous readings using standard deviation thresholds.
6. Reshape the dataset to analyze weekly health trends.
7. Simulate new patient health readings using NumPy’s random functions.'''

import numpy as np

health_data = np.array([
    [75, 120, 80, 98, 72, 118, 78],   # Patient 1: Heart rate, Systolic BP, Diastolic BP, Oxygen Level
    [85, 130, 85, 96, 80, 125, 82],   # Patient 2
    [90, 140, 90, 95, 88, 138, 85],   # Patient 3
    [60, 110, 70, 99, 68, 115, 76],   # Patient 4
    [100, 150, 95, 93, 110, 145, 92]  # Patient 5
])







'''Question : Sales Forecasting and Demand Analysis
A company tracks daily sales of multiple products in a 2D NumPy array, where each row represents a 
product and each column represents sales data over time. The company wants to forecast future 
demand.
Problem Statement:
Using NumPy, analyze sales trends and perform demand forecasting:
1. Create a 2D NumPy array to store sales data.
2. Find the total sales for each product.
3. Identify seasonal trends by reshaping data into weeks/months.
4. Sort products based on growth rate (percentage change over time).
5. Detect products with declining sales using trend analysis.'''


# import numpy as np

# # Step 1: Create a 2D NumPy array to store sales data
# # Assume we have 5 products, and sales data for 30 days (1 month)
# sales_data = np.array([
#     [150, 200, 250, 220, 180, 210, 240, 300, 320, 350, 400, 420, 430, 460, 490, 500, 480, 470, 440, 450, 470, 500, 530, 540, 550, 570, 600, 620, 640, 650],  # Product 1
#     [100, 120, 140, 130, 110, 140, 160, 180, 190, 220, 230, 250, 240, 260, 280, 300, 310, 320, 330, 340, 360, 380, 390, 400, 420, 430, 450, 460, 470, 490],  # Product 2
#     [90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 200, 220, 240, 250, 260, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420],  # Product 3
#     [200, 210, 250, 260, 220, 230, 240, 250, 270, 300, 330, 350, 360, 380, 400, 420, 430, 440, 460, 470, 480, 500, 520, 540, 550, 560, 580, 600, 620, 630],  # Product 4
#     [50, 70, 90, 100, 120, 130, 140, 150, 160, 180, 200, 220, 240, 250, 270, 290, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440],  # Product 5
# ])

# print(np.sum(sales_data,axis=1))

# print("Identify seasonal trends by reshaping data into weeks/months.")
# weekly_sales_data=sales_data.reshape(5,5,6)
# print(weekly_sales_data)



'''Question : Energy Consumption Monitoring in Smart Homes
A smart home system collects electricity usage data from different appliances. The data is stored in a 2D 
NumPy array, where each row represents an appliance and each column represents hourly energy 
consumption.
Problem Statement:
Using NumPy, analyze energy consumption patterns:
1. Create a 2D NumPy array to store energy consumption data.
2. Compute the total energy usage of each appliance.
3. Compute the average daily energy consumption per appliance.
4. Compute the cumulative energy usage over time.
5. Reshape the data to analyze weekly and monthly trends'''

weekly_data = energy_data.reshape(3, 2, 4)  # 3 appliances, 2 weeks, 4 hours each week
print("\nWeekly energy consumption data (reshaped):")
print(weekly_data)
