# tup = (1,) # when we use single value in tuple it will not be considered as tuple, it will be considered as integer. So to make it a tuple we need to add a comma after the value.

tup = (1, 2, 3, 4, "Hello", 5.6, True)

# print(type(tup), tup)
# print(tup[4])
# print(tup[-1])


# if 5.6 in tup:
#     print("Yes, 5.6 is present in the tuple")
# else:
#     print("No, 5.6 is present in the tuple")


tup2 = tup[1:4]
print(tup2) # (2, 3, 4)