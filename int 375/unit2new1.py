import numpy as np
# a=np.arange(1,7).reshape(2,3)
# b=print("Reference variable")
# print(a)
# # # print("\n-------------------------1")
# print(b)# it will give null because because print() does not return anything explicitly—it only prints the output to the console.
# # # print("\n-------------------------2")
# print(a is b)
# print(b is a)
# # print("\n-------------------------3")
# print("Shallow copy")
# c=a.view()#view():- if we change any value in a it will automatically get change in c,it doesnt copy the data
# it provide another reference to the same data
# # print("\n-------------------------4")
# print(a)
# # # print("\n-------------------------5")
# print(c)
# print("\n-------------------------6")
# print(a is c)
# print(c is a)
# print("\n-------------------------7")
# c[0][1]=22
# a[1][0]=43
# print(a)
# print(c)
# print("\n-------------------------8")
# print("Deep copy")
# d=a.copy()#When you use a.copy(), it creates a new array with the same data as a. This new array d is completely separate from a.
# # Any changes to d will not affect a, and changes to a will not affect d.
# print(a)
# print(d)
# print("\n-------------------------9")
# print(a is d)
# print(d is a)
# print("\n-------------------------10")
# d[0][1]=256
# print(a)
# print(d)




# l=[]
# n=int(input("Enter Number of elements"))
# for i in range(0,n):
#     l.append(int(input("Enter value")))
# a=np.array(l)
# print(a[::-1])
# print(a)

# #1D array
# a=np.array([1,3,4,5])
# print("#### 1D  ####")
# print(a*2)


# #22D array
# a=np.array([[1,2,3],[4,5,6],[1,2,3]])
# b=np.array([[1,2,3],[4,5,6],[1,2,3]])
# d=np.zeros([3,3],dtype=int)
# s=0
# for i in range(0,len(a)):
#     for j  in range(0,len(b)):
#         for k in range(0,len(b)):
#             d[i][j]=d[i][j]+(a[i][k]*b[k][j])

# print()
# print()
# print("#### 2D ####")
# print()
# print(a)
# print("---------")
# print(b)
# print("#--------a.b--------#")
# print(d) #MATRIXX  MULTIPLICATION
# print("#---------a@B----------#")
# print(a@b) #matrix multiplication 
# print("#------------a.dot(b)-----------#")
# print(a.dot(b))