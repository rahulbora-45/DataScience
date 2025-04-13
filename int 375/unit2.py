#numpy we used for the impplementation of array
# if we already had list why do we required array or numpy
# pandas-- analysis
#matplotlib,seaborn-- data vizualization

# python was not use for only data analysis for varius task we also used
import numpy as np

# # # # ----------------------method to create array
# a=np.array([1,2,3])  #1
# print("Array()",a)

# b=np.arange(6).reshape(2,3) #2==row ,3==col  #2

# ####np.arange(6):
# ####This generates a 1D array with values from 0 to 5 (not including 6), i.e., [0, 1, 2, 3, 4, 5].
# #####.reshape(2, 3):
# #####This reshapes the 1D array into a 2x3 2D array (matrix).
# #####The result of this operation is a 2D array
# print("Arange()",b)

# ### taking the col first is not possible while creating a array 
# but while displaying the array we can do it
# # string input
#  a=np.matrix('1 2; 3 4') #3
# a=np.matrix('1 2;3 4;5 6;7 8')
# # string and character are same is python
# print("Via string input: \n",a,"\n\n")

# //####----------------------------------------------------------------------------------------
# # array-like inout
# b=np.matrix([[5,6,7],[4,6,8]])  //This is a list of lists, where each inner list represents a row of the matrix.
# print("Via array-like input:\n",b)


# #//-----------------------------------------------------------------------------------------------
# b=np.zeros([2,3],dtype=float)
# print("Zeros",b)

# b=np.zeros([3,2],dtype=int) #dtype=int: This specifies the data type of the elements in the array. 
# #By default, np.zeros creates an array of floats (float64). However, here, dtype=int ensures that the array's elements are integers.
# print("Zeros",b)

# c=np.zeros([2,3])
# # print("Zeros",c)

# d=np.full([2,3],10)
# print("full",d)

# e=np.empty([3,3])
# print("empty",e)

# f=np.ones([2,3])
# print("ones",f)

# g=np.ones([2,3],dtype=int) #dtype = data type
# print("ones",g)

# h=np.eye(5,4) #it will create a matrix with 1 in its diagonal and other as zero
# print("eye",h)
# h=np.eye(3,3,dtype=int) #it will create a matrix with 1 in its diagonal and other as zero
# print("eye",h)

#####--------------------------------------------------

a=np.arange(6).reshape(2,3)

# print(a)
# print("max",np.max(a))
# print("min",np.min(a))
# print("sum",np.sum(a))
# print("sort",np.sort(a))
# print("abs",np.abs(-4))

# # print("abs",np.sqrt(a))
# print("Cummulative sum coloumn wise")
# print(a.cumsum(axis=0))
# print("Cummulative sum row wise:")
# print(a.cumsum(axis=1))

# print("Flatten function",a.flatten())#The flatten() method returns a new 1D array (a "flattened" version) of the original NumPy array a, with all the elements arranged in a single row.
# # It doesn't modify the original array a; instead, it creates and returns a new array that contains the same elements, but in one continuous line.
# print("Transpose function:\n",a.transpose())




 
# #Array Input
# l=[]
# for i in range(1,11):
#     l.append(int(input()))

# a=np.array(l)
# print(a)#it will print 1D array

# a.shape=(2,5)
# print(a)

# l=[]
# for i in range(1,11):
#     l.append(int(input()))
# a=np.array(l)
# a.shape=(2,5)
# print(a)


# ####Adding all the elements in an Array without using built in function
# ### 1D array
# a=np.array([1,2,3])
# s=0
# for i in a :
#     s=s+i
# print("Sum of all the elements are:",s)


# #2d array
# a=np.array(([1,2,3],[4,5,6]))
# s=0
# for i in range(0,2):
#     for j in range(0,3):
#         s=s+a[i][j]

# print("Sum of all the elements are: ",s)

