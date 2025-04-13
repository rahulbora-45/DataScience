# import pandas as pd
# # 
# print("Hello")

#  series and dataframe  differnce
# series we can work only  row only
# dataframe can work in both row and column wise
#  differemnce  between  series and array
#  see all the difference between series and dataframe'

import pandas as pd
# a  = pd.Series([1, 2, 3])
# print(a)

# print("--------------")

# b = pd.Series([1, 2, 3], index = ['A', 'B', 'C'])
# print(b)

# print("--------------")

# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print(s)

# print("--------------")

# data = {'a' : 0.0, 'b' : 1.0, 'c' : 2.0}
# s1 = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
# print(s1)

# list = ['g', 'e', 'k', 'a']
# s2 = pd.Series(list)
# print(s2)

# s3 = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])
# print(s3)

# l = ['c', 'e']
# print(s3['b'])
# print(s3['e'])
# print(s3[l])
# print(s3[['a','e']])#Single bracket [ ]:
# # # In a pandas Series, using a single bracket allows you to access a single element based on the index label.
# # # Double brackets are used when you want to select multiple elements at once from the Series,

# print("locatiom of b")
# print(s3.loc['b'])

# print("index location of b")
# print(s3.iloc[1])

# # c = pd.DataFrame(b)
# # print(c)

# d = pd.DataFrame(c,columns = ['Roll No'])

# print(d)
# d1 = pd.DataFrame(b,columns = ['Roll No'])
# print(d1)


import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])}
# print(pd.DataFrame(d))

# df = pd.DataFrame(d)
# print(df)
# print(df.loc['b'])
# print(df.iloc[2])
# print(df[2 : 4])

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a', 'b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a', 'b'])
df = df._append(df2)
print(df)

df = df.drop(0)
print(df)

