# def average(a, b):
#     print("the average is: ", (a + b) / 2)

# average(4, 6) # 5.0

# **********************************************************

# 1. Default Arguments:-

# def average(a=4, b=6):
#     print("the average is: ", (a + b) / 2)

# average() # example of default arguments, it will use the default values of a and b, which are 4 and 6 respectively. The output will be: "the average is: 5.0"
# average(10, 20) # example of default arguments, it will use the provided values of a and b, which are 10 and 20 respectively. The output will be: "the average is: 15.0"
# average(10) # example of default arguments, it will use the provided value of a, which is 10, and the default value of b, which is 6. The output will be: "the average is: 8.0"
# average(b=20) # example of default arguments, it will use the default value of a, which is 4, and the provided value of b, which is 20. The output will be: "the average is: 12.0"

# ------------------------------------------------------------------------------------------------------------------

# 2. Keyword Arguments:-

# def average(a, b):
#     print("the average is: ", (a + b) / 2)

# average(b=10, a=20) # example of keyword arguments, it helps provide arguments in any order, it will use the provided values of a and b, which are 20 and 10 respectively. The output will be: "the average is: 15.0"

# ------------------------------------------------------------------------------------------------------------------

# 3. Required Arguments:-

# def average(a= 1, b, c= 6):
#     print("the average is: ", (a + b + c) / 2)

# # average(10, 20) # example of required arguments, it will use the provided values of a and b, which are 10 and 20 respectively. The output will be: "the average is: 18.0"
# average(10, 20, 30) # example of required arguments, it will use the provided values of a, b and c, which are 10, 20 and 30 respectively. The output will be: "the average is: 30.0"
# average() # example of required arguments, it will raise a TypeError, indicating that the function call is missing a required positional argument 'b'.

# ------------------------------------------------------------------------------------------------------------------

# 4. Variable-length Arguments:-

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("the average is: ", sum / len(numbers))
# # average(10, 20, 30, 40, 50) # example of variable-length arguments, it will use the provided values of numbers, which are 10, 20, 30, 40 and 50 respectively. The output will be: "the average is: 30.0"
# average(10, 20) # example of variable-length arguments, it will use the provided values of numbers, which are 10 and 20 respectively. The output will be: "the average is: 15.0"
# average(10) # example of variable-length arguments, it will use the provided value of numbers, which is 10. The output will be: "the average is: 10.0"

# ------------------------------------------------------------------------------------------------------------------

# def name(**name):
#     print(type(name)) 
#     print("Hello,", name["fname"], name["mname"], name["lname"]) 

# name(mname = "Buchanan", lname = "Barnes", fname = "James") # this is an example of variable-length keyword arguments, it will use the provided values of name, which are "James", "Buchanan" and "Barnes" respectively. The output will be: "Hello, James Buchanan Barnes"

# ------------------------------------------------------------------------------------------------------------------

# return Statement

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # return 7  # if you use a return statement, the function will return the first return statement than you use multiple return statements, and the function will stop executing after the first return statement is executed. 
    return sum / len(numbers)
c = average(10, 20, 30, 40, 50)
print("the average is: ", c) # example of return statement, it will use the provided values of numbers, which are 10, 20, 30, 40 and 50 respectively. The output will be: "the average is: 30.0"