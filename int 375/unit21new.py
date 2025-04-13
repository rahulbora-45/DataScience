# import pandas as pd
# l=[12,25,56,88]
# df=pd.DataFrame(l,columns=['RollNo'])
# print(df)


# #Create series from array usinng pandas and numpy
# import pandas as pd
# import numpy as np
# data=np.array([90,75,50,66])
# s=pd.Series(data)
# print(s)

# # import pandas library and aliasingas pd
# import pandas as pd
# import numpy as np
# data=np.array(['a','b','c','d'])
# s=pd.Series(data,index=[100,101,102,103])
# print(s)

# '''We  passed the index values here.
# Now we can see the customized indexed values
#  in the output'''


# print("---------------------------------------------")
# #import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data={'a':0.,'b':1.,'c':2.}
# s=pd.Series(data)
# print(s)


# print("--------------------------------------------------")
#Observe-Dictionary keys are used to construct index
# Create series from dictionary using pandas
# import pandas as pd
# import numpy as np
# data={'Ahmed':92,'Ali':55,'Omar':83}
# s=pd.Series(data,index=['Ali','Ahmed','Omar'])
# print(s)

# print("--------------------------------------------------")
# #import the pandas library and aliasing as pd
# import pandas as pd
# import numpy as np
# data={'a':0.0,'b':1.0,'c':2.0}
# s=pd.Series(data,index=['b','c','d','a'])
# print(s)

# '''Observe -Index order is persisted and the missing element
# in fillef with NaN (Not a NUmber)'''
# # import the pandas library adn aliasing as pd
# import pandas as pd
# import numpy as np
# s=pd.Series(5,index=[0,1,2,3])
# print(s)

# # print("---------------------------------------------------")
# import pandas as pd
# # # #a simple list
# list=['g','e','e','k','s']
# list1=[1,2,3,4]

# # # # create series from a list
# ser=pd.Series(list)
# print(ser)
# ser1=pd.DataFrame(list1)
# print(ser1)##Notice how Pandas assigns an automatic column index (labeled 0 in this case) since no column name was provided.

####print("-------------------------------------------------------------")
import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# retrieve multiple elements

# When you use s['b'] or s['e'], you're accessing individual values from the Series.
# The output is just the value (e.g., 2 or 5), not the index, because you're directly requesting a single value at a specific index.
# If you want to see the index and value together, you can print the Series using s[['b']], s[['e']], or even s[['b', 'e']]
print(s['b'])
print(s['e'])

# When you select multiple elements from a Series using either a list of indices (like l = ['c', 'e']) or 
# by directly passing multiple indices (like ['a', 'e']), Pandas preserves both the index and the value.
l=['c','e']
print(s[l])
print(s[['a','e']])
# When you select elements from a Series, Pandas preserves both the values and
# their associated indices. This means you get the index-value pairs in the output, even when you're selecting specific values
# print("-------------------------------------------------------------")










