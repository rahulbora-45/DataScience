# #Demonstrating Basic Data Types in python
# #integer
# age=25
# print(f"Age:{age},Type: {type(age)}")
# #float
# height=5.9
# print(f"Height : {height} ,Type: {type(height)}")
# #string
# name="Alice"
# print(f"Name: {name} ,Type: {type(name)} ")
# #Boolean
# is_student=True
# print(f"Is Student: {is_student},Type:{type(is_student)}")
# #List
# fruits=["apple","banana","cherry"]
# print(f"Fruits: {fruits},Type:{type(is_student)}")
# #list
# fruits=["apple","banana","charry"]
# print(f"Fruits: {fruits},Type:{type(fruits)}")
# # tuple
# coordinates=(10.5,20.8)
# print(f"Coordinates:{coordinates},Type: {type(coordinates)}")
# #set
# unique_numbers={1,2,3,4,5}
# print(f"Unique Numbers: {unique_numbers},Type:{type(unique_numbers)}")
# # dictionary
# student={"name":"Alice","age":25,"is_student":True}
# print(f"Student: {student},Type:{type(student)}")

# # #Demonstrating type conversion
# #Integer to String
# age_str=str(age)
# print(f"Age(String):{age_str},Type:{type(age_str)}")
# # string to integer
# age_int =int(age_str)
# print(f"Age (Integer):{age_int},Type:{type(age_int)}")
# # string to float
# height_str="5.9"
# height_float =float(height_str)
# print(f"Height (Float):{height_float},Type:{type(height_float)}")
# #List to Set
# unique_fruits= set(fruits)
# print(f"Unique Fruits :{unique_fruits},Type:{type(unique_fruits)}")




# #  write a prorgam to find even or odd
# number=int(input("Enter number"))

# if(number%2==0):
#     print("Number is even")
# else:
#     print("Numbwr is  odd")




# n=int(input(" "))
# print(f"Table of {n}: ")
# for i in range(1,10):
#     print(f"{n} X{i} = {n*i}")




# # ### Python Control Structures Demonstration

# #conditional Statements
# print(" Conditional Statements: ")
# x=10
# if(x>0):
#     print(f"{x} is posiitive")
# elif x==0:
#     print(f"{x} is zero.")
# else:
#     print(f"{x} is negative.")
# print("\nLoops:")

# #For Loop
# print("For Loop Example:")
# for i in range(5):
#     print(f"Iteration {i}")


# # while loop
# print("\nWhile Loop Example: ")
# count =0
# while count<3: #Loop until th4 condition is False
#     print(f"Count is {count}")
#     count +=1

# print("\nControl Flow Modifiers:")


# #Break Statement
# print("Break Statement")
# for i in range(5):
#     if i ==3:
#          print("Breaking the loop at i=3")
#          break
#     print(i)

# #  continue statement
# print("\nContinue Example: ")
# for i in range(5):
#     if i==2:
#         print("Skipping iteration for i=2")
#         continue
#     print(i)

# # Pass statrement
# print("\Pass Example: ")
# for i in range(3):
#     if i==1:
#         pass #Placeholder for future code
#     print(f"i = {i}")

# # Nested Loops
# print("\nNested Loops Example: ")
# for i in range(3):
#     for j in range(2):
#         print(f"Outer loop:{i},Inner loop:{j}")

# #Match-Case Statetemnt (introduced in Python 3.10)
# print("\nMatch-Case Statemet Example:")
# status_code=200
# match status_code:
#     case 200:
#         print("OK")
#     case 404:
#         print("Not Found")
#     case 500:
#         print("Server Error")
#     case _:
#         print("Unknown Status code")

# print("\nAdditional Examples: ")
# #Else witih Loops
# print("else with Loops: ")
# for i in range(3):
#     print(i)
# else:
#     print("Completed the loop without  breaking")

# print("\nInfinite Loops Example(with break to avoid infinite execition: ")
# count =0
# while True:
#     print(f"Infinite loop count :{count}")
#     count +=1
#     if count==3:
#         print("Breaking out the infinite loop.")
#         break




# n=int(input("Enter n: "))
# sum=0
# for i in range(0,n):
#     grade=int(input("Enter grade: "))
#     sum+=grade

# avg=sum/n
# print("Avg grade: ",avg)

# if(avg >=90 and avg<=100):
#     print("A")
# elif(avg >=80 and avg<=89):
#     print("B")
# elif(avg >=80 and avg<=89):
#     print("C")
# elif(avg >=70 and avg<=79):
#     print("D")
# elif(avg >=60 and avg<=69):
#     print("B")
# else:
#     print("F")



# n=int(input("Enter the input: "))

# for i in range (0,n):
#     if(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     elif(i%5==0 and i%3==0 ):
#         print("FizzBuzz")
#     else:
#          print (i)
    
# #in oytton we can use construtor and destructor for making a function
# #Basis Function
# def greet():
#     print("Welcome to the function demo!")
# #Function with Parameters and return values

# def multiply(a,b):
#     return a*b
# #Function with default parameter Value

# def power(base,exponent=2):
#     return base ** exponent


# #variable-Length Arguement
# def sum_all(*numbers):
#     return sum(numbers)


# #Recursive Function
# def factorial(n):
#     if n==0:
#         return 1
#     return n* factorial(n-1)

# #Generator Fuunction

# def even_numbers(limit):
#     for i in range(limit):
#         if i%2==0:
#             yield i

        
# # #Generator Function

# #Nested Function 
# def outer_function(message):
#     def inner_function():
#         print(f"Message from inner function: {message}")
#     inner_function()
#     #Basic Function
#     greet()
#     #Fuunction with Parameters and return values
#     print(" Multiply 3 and 4 :",multiply(3,4))
#     #Function with Default Parameter Value
#     print("2 raised to 3:",power(2,3))
#     print("Sqaure of 5 (default exponent):",power(5))
#     #varialble-Length Arguement
#     print("Sum of 1 ,2 ,3,4,5:",sum_all(1,2,3,4,5))
#     #Recursive Function
#     print("Factorial of 5:",factorial(5))
#     #Generator Function
# print("Even numbers up to 10::",list(even_numbers(10)))
# #call the outer function
# outer_function("Hello from nested function!")



# ### in pythonwe have 8 precision or till the buffer overflow in some cases it is 15 also