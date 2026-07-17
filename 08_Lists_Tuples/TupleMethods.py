tup = ("india", "russia", "germany", "brazil", 1, 55, 6000, 6.5, 55)

# 1. count() 

# print(tup.count(55)) # 2
# --------------------------------------------------------------------

# 2. index()

# print(tup.index(1)) # 4
# --------------------------------------------------------------------

# 3. len()

# print(len(tup)) # 9
# --------------------------------------------------------------------

# 4. min()
# tup2 = (1, 55, 6000, 6.5, 55, -99) # it returns the minimum value from the tuple. -> -99
# tup2 = ("india", "russia", "germany", "brazil") # in real world, it returns the minimum value based on alphabetical order. -> "brazil"

# print((min(tup2))) 
# --------------------------------------------------------------------

# 5. max()

# tup2 = (1, 55, 6000, 6.5, 55, -99) # it returns the maximum value from the tuple. -> 6000
# tup2 = ("india", "russia", "germany", "brazil") # in real world, it returns the maximum value based on alphabetical order. -> "russia"

# print((max(tup2))) 
# --------------------------------------------------------------------

# 6. sum()

# numbers = (1, 55, 6000, 6.5, 55)

# print(sum(numbers)) # Output: 6117.5
# --------------------------------------------------------------------

# 7. sorted()

# tup = (5, 2, 8, 1, 3)

# result = sorted(tup)

# print(result) # [1, 2, 3, 5, 8] # the sorted() function returns a new sorted list from the items in the tuple.
# print(tup) # (5, 2, 8, 1, 3) # The original tuple remains unchanged.

# names = ("Rahul", "Amit", "Subhajit", "Ankit") #  use this in sorted() function to sort the names in alphabetical order.

# print(sorted(names)) # ['Amit', 'Ankit', 'Rahul', 'Subhajit']
# --------------------------------------------------------------------

# 8. any()
# tup = (False, False, False) # Output: False # It returns True if any item in the tuple is true. If the tuple is empty, it returns False.
# tup = (False, False, True) # Output: True # It returns True if any item in the tuple is true. 
# tup = (0, 0, 5) # Output: True
# tup = (0, 0, -5) # Output: True
# tup = (0, 0, 0) # Output: False

# print(any(tup)) 
# --------------------------------------------------------------------

# 9. all()

# tup = (True, True, True) # Output: True
# tup = (True, True, False) # Output: False
# tup = (1, 2, 3)  # Output: True
# tup = (0, 0, 0)  # Output: False

# print(all(tup))
# --------------------------------------------------------------------

# 10. del()

# name = "Subhajit"
# name = (1, 2, 3, 4, 5)

# del name

# print(name)
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------