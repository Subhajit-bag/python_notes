number = [1, 2, 3, 4, 5, "Hello", 6.7, True]

# print(number) # [1, 2, 3, 4, 5, "Hello", 6.7, True]
# print(type(number)) # <class 'list'>
# print(number[0]) # 1
# print(number[5]) # Hello

# print(number[-2]) # 6.7 <- this is called negative indexing.
# print(number[8-2]) # 6.7
# print(number[len(number)-2]) # 6.7

# ************************************************************************************

# if "Hello" in number:
#     print("Yes")
# else:
#     print("No")

# ************************************************************************************

# same thing can be done with string as well. 

# if "Hel" in "Hello":
#     print("Yes")    
# else:
#     print("No")

# ************************************************************************************

# print(number) # [1, 2, 3, 4, 5, "Hello", 6.7, True]
# print(number[:]) # [1, 2, 3, 4, 5, "Hello", 6.7, True]
# print(number[1:-1]) # [1, 2, 3, 4, 5, "Hello", 6.7, True]
# print(number[1:9:2]) # [2, 4, "Hello", True] <- this is called slicing.

# --------------------------------------------------------------------------------------------------------

# List Comprehension

# lst = [i for i in range(4)] # this is called list comprehension. It is a concise way to create lists in Python. The syntax is [expression for item in iterable]. In this case, it creates a list of numbers from 0 to 3 (4 is not included).
# lst = [i*i for i in range(4)] # this will create a list of squares of numbers from 0 to 3. The output will be [0, 1, 4, 9].
# lst = [i*i for i in range(10)] # this will create a list of squares of even numbers from 0 to 9. The output will be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81].
lst = [i*i for i in range(10) if i%2 == 0] # this will create a list of squares of even numbers from 0 to 9. The output will be [0, 4, 16, 36, 64].
print(lst) 




