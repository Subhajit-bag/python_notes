# l = [1, 2, 3, 4, 5]

# print("the data is : ", l)

# *************************************************

# 1. append() -> It adds an element at the end of the list.

# l.append(6)
# print("the data after append is : ", l) #  [1, 2, 3, 4, 5, 6]

# *************************************************

# 2. sort() -> It sorts the list in ascending order.

# l = [12, 2, 333, 4, 1, 5] 

# l.sort() 
# print("the data after sort is : ", l)  # [1, 2, 4, 5, 12, 333]

# l.sort(reverse=True) # it sorts the list in descending order.
# print("the data after sort is : ", l)  # [333, 12, 5, 4, 2, 1]

# *************************************************

# 3. reverse() -> It reverses the order of the list.

# l = [1, 2, 3, 4, 5]
# print("the data is : ", l) # [1, 2, 3, 4, 5]

# l.reverse()
# print("the data after reverse is : ", l) # [5, 4, 3, 2, 1]

# *************************************************

# 4. index() -> It returns the index of the first occurrence of the specified value.

# l = [1, 2, 3, 4, 5]
# print("the data is : ", l) # [1, 2, 3, 4, 5]

# print("the index of 3 is : ", l.index(3)) # 2

# *************************************************

# 5. count() -> It returns the number of occurrences of the specified value.

# l = [1, 2, 3, 4, 5, 3, 3]
# print("the data is : ", l) # [1, 2, 3, 4, 5, 3, 3]

# print("the count of 3 is : ", l.count(3)) # 3

# *************************************************

# 6. copy() -> It returns a shallow copy of the list.

# l = [1, 2, 3, 4, 5]

# m = l.copy()
# m[0] = 0 
# print(l) # [1, 2, 3, 4, 5]
# print(m) # [0, 2, 3, 4, 5]

# *************************************************

# 7. insert() -> It inserts an element at the specified position.

# l = [1, 2, 3, 4, 5]

# print("the data is : ", l) # [1, 2, 3, 4, 5]

# l.insert(2, 10) # it helps to insert the element 10 at index 2
# print("the data after insert is : ", l) # [1, 2, 10, 3, 4, 5]

# *************************************************

# 8. extend() -> It adds the elements of a list (or any iterable), to the end of the current list.

l = [1, 2, 3, 4, 5]

n = ["subhajit", "suravi", "why can't you love me and why ..."]

# l.extend(n)
# print("the data after extend is : ", l) # [1, 2, 3, 4, 5, 'subhajit', 'suravi', "why can't you love me and why ..."]

k = l + n

print("the data after extend is : ", k) # in this case, it will create a new list and store the data in it. [1, 2, 3, 4, 5, 'subhajit', 'suravi', "why can't you love me and why ..."]

