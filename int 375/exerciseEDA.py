###Write  a python programm to perform EDA using  iris dataset
#####1)use Boxplot  2)User scatterplot for visualization 3)use hist 4) use heatmap

import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset('iris')

print(data.head())
print(data.tail())
print(data.describe())
# iris.info()
plt.figure(figsize=(5,6))
# sns.scatterplot(data=iris,x='sepal_length',y='sepal_width',hue='species',palette='PuOr')
# # plt.show()


# # ### histgoram

# # # plt.hist(data.petal_length,bins=10)

# # ##or
# # plt.hist(data=data,bins=10,x='petal_length',edgecolor='black')
# plt.show()

# #### heatmeap

# corr=iris.corr(numeric_only=True)
# sns.heatmap(corr,annot=True)
# plt.show()