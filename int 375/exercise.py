import numpy as np



# /// / / / using  arnage function
# using arrnage without reshape will create  only 1d array

# 2d array
b=np.arange(6).reshape(2, 3) #6 is the total number of  elements (2X3)
print("2D: ",b);


# 3d array
b=np.arange(24).reshape(2, 3,4) #24 is the total number of  elements (2X3)
print("3D: ",b);




# # // // / / using  array function
# a=np.array([4,5,6,7])
# print("1D Array",a)


# b=np.array([[1,2,3],[4,5,6]]) #2saure bracket
# print("2D",b)

# c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]]); # 3 sqaure bracket
# print("3D",c)

a=np.array([[[1,2,9]]])
