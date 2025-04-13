# """You are working as a data anakyst for a company that deals with largr datasets.Your team a 2D NumPy
# containing customer transaction data,where each row represents a different customer and columns represent transaction amounts in different months
# Using Numpy functions: 
# 1.Find the max and min and total transaction amount across all customers.
# 2.Compute the cumulativr sum of transaction coumn-wise
# 3/Flatten the   2D array into a 1D array and sort the transactions in ascending order.
# 4.Transform dataset by reshaping it into a different structure'
# Write Python code to achieve the tasks and explain the significance of each function in data transformation

# """

# import numpy as np

# customer=int(input("Enter the number of customers: "))
# months=int(input("Enter the number of months: "))

# transaction_data=[]
# for i in range(customer):
#     customer_transaction=[]
#     print(f"Enter transaction for customer {i+1}:")
#     for j in range(months):
#         transaction=int(input(f"Months{j+1}:"))
#         customer_transaction.append(transaction)
#     transaction_data.append(customer_transaction)


# a=np.array(transaction_data)
# print(a)

# print("maximum: ")
# print(np.max(a))

# print("minimum: ")
# print(np.min(a))

# print("total:")
# print(np.sum(a))

# print(np.cumsum(a,axis=0))

# d=a.flatten()
# print(d)
# # ascending order
# print(np.sort(d))
# # descending order
# print(np.sort(d)[::-1])

# # reshaping the data
# print("reshaping the data")
# reshaped_data=np.reshape(a,(2,-1))




# '''Question 2: Matrix Operations and Computation
# A company is working on an AI-based recommendation system and needs to perform several matrix
# operations. The dataset consists of two matrices:  Matrix A (User-Product Interaction): 
# Contains ratings given by users to different products.  Matrix B (Product-Feature Mapping): Contains product attributes that help in recommendations. Using NumPy:
# 1. Perform element-wise multiplication of the user-product interaction matrix with another similar
# matrix. 2. Compute the matrix multiplication of A and B using two different NumPy functions. 3. Find the transpose of matrix A . 4. Identify the shape, number of dimensions, and data type of matrix B. Write Python code to perform these operations and explain how these transformations are used in
# recommendation systems. # Defining matrices
# A = np.array([[5, 3, 2], [4, 1, 5], [3, 2, 4]]) # User-Product Interaction
# B = np.array([[1, 2], [3, 4], [5, 6]]) # Product-Feature Mapping'''

# import numpy as np

# A=np.array([[5,3,2],[4,1,5],[3,2,4]])
# B=np.array([[1,2],[3,4],[5,6]])

# # print("elementary multiplication of A: ")
# # # print(A*A)
# # print(np.multiply(A,A))

# # print("Matrix multiplcation of A and B with different function")
# # print(A@B)
# # print(A.dot(B))


# print("Transpose of Matrix A: ")
# print(np.transpose(A))

# print("Identify the shape,number of dimensions and datatype of matrix B")
# print(B.shape)
# print(B.ndim)
# print(B.dtype)

import numpy as np

students=int(input("Enter the no. fo students: "))
subjects=int(input("Enter the no.of subjects: "))

scores=[]
for i in range(students):
    students_score=[]
    print(f"Enter the scores for Student{i+1}:")
    for j in range(subjects):
        score=int(input(f"Enter score for Suject{j+1}:"))
        students_score.append(score)
    scores.append(students_score)

marks=np.array(scores)
print(marks)

# print("reshaping the array")
# reshaped_array=np.reshape(marks,(2,-1))
# print(reshaped_array)

# print("highest and lowest score across all students and subjects. ")
# print(np.max(marks))
# print(np.min(marks))

# # 4. Calculate the total and average scores of students
# total=np.sum(marks,axis=1)
# average=np.mean(marks,axis=1)
# print("Total Score: ",total)
# print("average: ",average)

# # 6. Sort student scores in ascending order for each subject (column-wise)

# print("Sort student scores in ascending order for each subject:")
# print(np.sort(marks,axis=0))

# print("Compute the square root of each score")
# print(np.sqrt(marks))

# print("Find the cumulative sum of scores row-wise and column-wise.")
# print(np.cumsum(marks,axis=1))
# print(np.cumsum(marks,axis=0))

# print("Transpose the dataset to swap rows and columns for analysis.")
# print(np.transpose(scores))


print("Perform matrix multiplication to analyze weighted scores.")
weight=[]
for i in range (subjects):
    weight.append(float(input(f"Enter the weight from subject{i+1}: ")))

print(np.array(weight))

print(weight*marks)
# print(marks*weight)

# print("Use element-wise operations to scale or modify scores.")

# scaled_scores=marks*1.1
# print(scaled_scores)
# print("Extract scores of a specific student.")
# print(marks[1:2,1:2])

# print("Extract marks of a particular subject using column slicing.")
# print(marks[:,0:1])

# print("Allow users to input scores and reshape them into a structured NumPy array")