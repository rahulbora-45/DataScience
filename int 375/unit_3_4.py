import seaborn as sns
import matplotlib.pyplot as plt

###LOad the bult-in 'iris' dataset
iris=sns.load_dataset('iris')


### 1.Scatter plot

plt.figure(figsize=(7,5))
sns.scatterplot(x='sepal_length',y='sepal_width',hue='species',style='species',data=iris,palette='deep')

plt.title("Scatter Plot of Sepal Length vs Sepal WIdth")
plt.show()

### 2.Line PLot
plt.figure(figsize=(7,5))
sns.lineplot(x='sepal_length',y='sepal_length',hue='species',marker='o',data=iris,palette='tab10')
plt.tile('Line Plot of Sepal Length vs Petal Lenght by Species')
plt.show()


#########Why do we use box plot??


import pandas as pd

student = [1,2,3,4,5]
maths = [87,90,89,78,89]
science = [78,89,90,89,90]

dict1 = dict({"Student":student,"Maths":maths,"Science":science})

df = pd.DataFrame(dict1)

print(df.corr())
print(df.cov())


