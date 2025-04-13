import pandas as pd
'''A school collects student marks in different subjects and stores them in a Pandas Series.
Analyze the student performance based on the given data.
Data:
import pandas as pd
marks = pd.Series([85, 90, 78, 92, 88], index=['Alice', 'Bob', 'Charlie', 'David', 'Emma'])
print(marks)
Questions:
1. How do you access Charlie’s marks using index labels?
2. Retrieve the marks of Alice and Emma using multiple indices.
3. What will marks.loc['Bob'] return?
4. Add a new student Frank with marks 80 to the Series.
5. Compute the average marks of all students.'''



# marks=pd.Series([85,90,78,92,83],index=['Alice', 'Bob', 'Charlie', 'David', 'Emma'])

# print(marks.loc['Charlie'])

# print(marks.loc[['Alice','Emma']])

# bob_marks=marks.loc['Bob']
# print(bob_marks)

# marks['Frank']=80
# print(marks)

# average=marks.mean()
# print(average)



# '''A company maintains salary records of its employees in a Pandas DataFrame.
# Data:
# data = {'Employee': ['John', 'Anna', 'Mike', 'Sara'],
#  'Salary': [50000, 62000, 58000, 75000]}
# df = pd.DataFrame(data)
# print(df)
# Questions:
# 1. How do you retrieve the salary of Mike using index-based selection?
# 2. Add a new column "Department" with values ['HR', 'Finance', 'IT', 'Marketing'].
# 3. Compute the average salary of all employees.
# 4. Identify the employee with the highest salary.
# 5. Sort the DataFrame based on Salary in descending order.'''

# data = {'Employee': ['John', 'Anna', 'Mike', 'Sara'],
#  'Salary': [50000, 62000, 58000, 75000]}
# df = pd.DataFrame(data)
# print(df)
# print(df.loc[2,'Salary'])

# df['Department']=['HR','Finance','IT','Marketing']
# print(df)

# print(df['Salary'].mean())


# print(df.loc[df['Salary'].idxmax()])
# print(df.sort_values(by='Salary',ascending=False))



# '''A retail store keeps track of its product inventory using a Pandas Series.
# Data:
# inventory = pd.Series({'Laptops': 15, 'Mobiles': 30, 'Tablets': 12, 'Headphones': 50})
# print(inventory)
# Questions:
# 1. How do you access the inventory count of Tablets?
# 2. Add a new product Smartwatches with stock 20.
# 3. Reduce the stock of Mobiles by 5 (update the value).
# 4. Retrieve the stock of Laptops and Headphones using indexing.
# 5. Find the total number of items available in the store.'''

# import pandas as pd
# inventory = pd.Series({'Laptops': 15, 'Mobiles': 30, 'Tablets': 12, 'Headphones': 50})
# print(inventory)

# # print(inventory.loc['Tablets'])

# # inventory['Smartwatches']=20
# # print(inventory)

# # inventory['Mobiles']-=5

# # print(inventory)

# print(inventory.loc[['Laptops','Headphones']])

# print(inventory.sum())



'''A library keeps track of the number of copies available for different book genres using a Pandas Series.
Data:
books = pd.Series({'Fiction': 25, 'Non-Fiction': 18, 'Science': 12, 'History': 20})
print(books)
Questions:
1. How do you check the number of available Science books?
2. Add a new genre "Philosophy" with 10 books.
3. Update the Fiction genre by reducing 5 books.
4. Retrieve the book counts for Non-Fiction and History using indexing.
5. Calculate the total number of books in the library.'''

# books = pd.Series({'Fiction': 25, 'Non-Fiction': 18, 'Science': 12, 'History': 20})
# print(books)

# # print(books.loc['Science'])

# # books['Philosophy']=10
# # print(books)

# # books['Fiction']-=5
# # print(books)

# print(books.loc[['Non-Fiction','History']])

# print(books.sum())


'''A grocery store tracks the stock levels of different items using a Pandas Series.
Data:
grocery_stock = pd.Series({'Rice': 100, 'Wheat': 80, 'Sugar': 50, 'Milk': 200})
print(grocery_stock)
Questions:
1. How do you check the current stock of Sugar?
2. Add a new product "Eggs" with 150 stock.
3. Reduce the stock of Milk by 20.
4. Retrieve the stock of Rice and Wheat using indexing.
5. Find the total stock of all grocery items in the store.'''
import pandas as pd
grocery_stock = pd.Series({'Rice': 100, 'Wheat': 80, 'Sugar': 50, 'Milk': 200})

print(grocery_stock)

print(grocery_stock.loc['Sugar'])

grocery_stock['Eggs']=150
print(grocery_stock)

grocery_stock['Milk']-=20
print(grocery_stock)

print(grocery_stock.loc[['Rice','Wheat']])

print(grocery_stock.sum())