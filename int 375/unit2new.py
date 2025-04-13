import numpy as np
# # #### dtype is the basic numpy function and type is the basic python function
# a=np.array([[1,2,3],[4,5,6],[8,9,10]])
# b=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a-b)#Subtraction----
# print(a**2)## raise to power
# print(a*b) ##element multiply-----

# The above operator perform operations when two  arrays have the same shape


# When they dont have same shape the below operator are used

#------------------------------------------------------
# a=np.arange(6).reshape(2,3)
# print(a.ndim) # it gives the dimension
# b=np.arange(10,22,2).reshape(3,2)
# print(b.ndim)
# print(a@b)#Matrix  Multiplication @is the operator for matrix multiplication in Numpy
# # # here b@a becuase  b=[3,2]and a=[2,3] which satisfy 2d matrix multiplication condition

# print(a.dot(b))
# #Matrix Multiplication-------------------

# # ###Array Dimensions
a=np.arange(25).reshape(5,5)
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.dtype.name)
# print(a.itemsize)
# print(type(a))


# ########Indeexing and slicing
# print(a)
# print("------------------------") 
# print(a[1][0])
# print("------------------------") 
# print(a[1:4])#row slicing'
# print("------------------------") 
# print(a[:,1:2]) # row,coloumn
# print("------------------------") 
# print(a[1:4,0:1])#column slicing
