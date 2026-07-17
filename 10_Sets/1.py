fruits = {"Apple", "Banana", "Mango", "Apple"}

# print(fruits) # {'Banana', 'Mango', 'Apple'}
# **********************************************************************************************
s = {2, 4, 2, 6}

# print(s) # {2, 4, 6}
# **********************************************************************************************

thisset = {"apple", "banana", "cherry", True, 1, 2}

# print(thisset) # {True, 2, 'cherry', 'banana', 'apple'} <- Sets do not maintain the order of elements. You cannot expect items to remain in the same sequence in which they were added
# **********************************************************************************************

# subhajit = {} # <class 'dict'> <- because curly braces {} default to an empty dictionary in Python.
subhajit = set() # <class 'set'> <- this is a correct way to create an empty set
print(type(subhajit))
# **********************************************************************************************

# Accessing Data use for loop
thisset = {"apple", "banana", "cherry", True, 1, 2}

for i in thisset:
    print(i)