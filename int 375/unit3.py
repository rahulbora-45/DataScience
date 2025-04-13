# # Data analysis--> just to get insights of the data
# #when we want to divide the data in terms of time we used-line chart
# #when the data are in discreet then we used bar diagram
# #For continuous data we used ->histogram
# #for portion we used ->pia chart
# # #when we have to find relationship between two  numerical values(eg directly poportional or inversely proportional) then we used scatter plot

# # ## for simple dataset or simple visualization we use matplotlib for advanced visualization we use seaborn

# import matplotlib.pyplot as plt  ## it means importing pyplot module from matplotlib

# #Create data
# x=[1,2,3,4,5]
# y=[10,20,25,30,40]

# #Create a plot
# #plt.plot(): This function plots a line graph using the provided x and y data points.
# plt.plot(x,y,marker="^",linestyle="-",color='b',label='Line 1')
# ####The label parameter is used to specify a name for the plotted line.

# ###the marker is used to display individual data points as symbols 
# # # '''marker:
# # # 'o'     Circle
# # # '^       Triangle (Up)
# # # 'v'     Triangle(Down)
# # # 's       Square
# # # '*'      Star
# # # 'D'      Diamond
# # # 'x'      Cross
# # # '+'     Plus sign
# # # 'p'     Pentagon
# # # 'h'     Hexagon
# # # '.'     Small dot'''

# # # #Add labels and title
# plt.xlabel("X-axis Label")
# plt.ylabel("Y-axis Label")
# plt.title("Basic Line Plot")

# #Show legend
# plt.legend()## This function adds a legend box to the plot, which helps the viewer understand what each plot element (line, marker, color, etc.) represents.

# ###what is lgend????
# #Display the plot
# plt.show()





# import matplotlib.pyplot as plt

# #Data 
# categories=['A','B','C','D']
# #  we have some category so that we have an categprical output
# values=[10,20,15,25]

# #Create bar chart
# plt.bar(categories,values,color='blue')

# #Add labels and title
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.title("Basic Bar Chart")

# #Show the plot

# plt.show()





# # ### code to check how many color code avaliabale

import matplotlib.colors as mcolors
colors=mcolors.CSS4_COLORS #Dictionary of named colors
print(list(colors.keys()))



# import matplotlib.pyplot as plt

# #sample data
# x=[1,2,3,4,5]
# y=[10,20,15,25,30]
# #Create  a plot
# plt.plot(x,y,marker='o',linestyle='-',color='b',label='Line 1')
# #Create a scatter plot
# plt.scatter(x,y,marker='o',s=200,color='b') #s sets the marker size

# #Add labels and title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Scatter Plot Diagram")

# plt.legend()
# #Display the plot
# plt.show()


# # # distribution of data =scatterplot
# # #corelation and regression then we use both scatterplot and line diagram

# Correlation:Measures relationship strength                    
# Regression:Predicts values


# ### why it is called hexadecimal color coding??


# # #_------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import numpy as np
# #Sample data

# ## np.random.randn() is a function from NumPy that generates normally distributed random numbers.
# data=np.random.randn(1000) #1000 random numbers



# #Create histogram
# plt.hist(data,bins=10,color='forestgreen',edgecolor='black')
# ''' for eg  : in  the diagram the x axis range is -3 to 3 if we set the bin =10 then it will
# divide -3 to 3 range into 10 eual parts
#                 if we put the bin size to 200 then it will divide -3 to 3 into 200 equal parts
# '''

# '''the bins parameter determines the number of intervals (bins)
# used to groups to the data.Each bin represents a range values,and the height of the bar shows how many data points fall within that range'''

# #Add labels and title
# plt.xlabel('Value')
# plt.ylabel('Frquency')
# plt.title('Histogram')+
# plt.show()


# ####----------------------

# import matplotlib.pyplot as plt
# # #Data
# list1=['Apple','Banana','Cherry','Dates']  ##labels for silces
# sizes=[30,20,40,10]
# # #Create Pie Chart
# plt.pie(sizes,labels=list1,autopct='%1.1f%%')##The first 1 in '%1.1f%%' is the minimum width of the number before the decimal point.

# # #autopct:The format string defines how the percentanges appear
# ####he pie chart will have four slices with labels: "Apples", "Bananas", "Cherries", and "Dates".
# # # labels=labels: The labels argument assigns labels to the slices. In this case, the labels list is assigned as ['Apple', 'Banana', 'Cherry', 'Dates'].
# # # Each label will be displayed next to its corresponding slice in the pie chart.

# # # #Add titile
# plt.title("Fruits Distribution")

# #Show the plot
# plt.show()

# plt.pie(sizes,labels=list1,autopct='%1.1f%%',startangle=90)
# ##autopct is use to display the percentage value
# ### here startangle=90 degree means it will start from the origin(0,0)
# ### start angle defines from which place the first slice will start
# # startangle determines the starting angle of the first slice of the pie chart.
# # The angle is measured counterclockwise from the positive x-axis (0 degrees).

# plt.legend(title="Fruits")

# plt.title("Pie chart with Legend")

# plt.show()
