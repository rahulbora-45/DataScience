##Outliers

####For even number
import numpy as np
import matplotlib.pyplot as plt
#sample dataset
data=np.array([10,12,14,15,18,21,22,25,28,2,-10,30])

# # 1.IQR Method
# Q1=np.percentile(data,25)
# Q3=np.percentile(data,75)
# IQR=Q3-Q1
# lower_bound=Q1-1.5*IQR
# upper_bound=Q3+1.5*IQR
# outliers_iqr=data[(data<lower_bound)|(data>upper_bound)]

# print(outliers_iqr)

# plt.figure(figsize=(6,4))
# plt.boxplot(data,vert=False)
# plt.xlabel("Values")
# plt.title("Box plot for outlier ddetection")
# plt.show()


# ####For odd number
# import numpy as np
# import matplotlib.pyplot as plt
# #sample dataset
# data=np.array([10,12,14,15,18,21,22,25,28,2,-10])

# # 1.IQR Method
# Q1=np.percentile(data,25)
# Q3=np.percentile(data,75)
# IQR=Q3-Q1
# lower_bound=Q1-1.5*IQR
# upper_bound=Q3+1.5*IQR
# # outliers_iqr=data[(data<lower_bound)|(data>upper_bound)]

# print(outliers_iqr)

# ##2. Z-Score Method(Using Sample Standard Deviation)
# mean=np.mean(data)
# std_dev=np.std(data,ddof=1) ## Use sample standard deviation
# z_scores=(data-mean)/std_dev
# outliers_z=data[np.abs(z_scores)>3]  ##Outliers: Z>3 or Z<-3
# print(outliers_z)



################
import seaborn as sns
data=sns.load_dataset('iris')
# print(data.describe())
mean_i=data['sepal_length'].mean()
std_i=data['sepal_length'].std(ddof=1)
z_score=(data['sepal_length']-mean_i)/std_i
print(z_score)
outliers=data[np.abs(z_score)>3]
print(outliers)