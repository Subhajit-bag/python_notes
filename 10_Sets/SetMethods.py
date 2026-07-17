# 1. union() :-
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# print(s1.union(s2)) # {1, 2, 3, 5, 6, 7}
# -------------------------------------------------------------

# 2. update() :-
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

# print(x) # {'cherry', 'google', 'apple', 'microsoft', 'banana'}
# -------------------------------------------------------------

# 3. intersection() :-
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

# print(z) # {'apple'}
# -------------------------------------------------------------

# 4. intersection_update() :- 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

# print(x)
# -------------------------------------------------------------

# 5. symmetric_difference() :- 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

# print(z)
# -------------------------------------------------------------

# 6. difference() :- 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

# print(z)
# -------------------------------------------------------------

# 7. isdisjoint() :-
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

# print(z)
# -------------------------------------------------------------

# 8. issuperset() :-
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

# print(z)
# -------------------------------------------------------------

# 9. issubset() :-
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

# print(z)
# -------------------------------------------------------------

# 10. add() :- 
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")

# print(fruits)
# -------------------------------------------------------------

# 11. discard() :- / remove() :-
fruits = {"apple", "banana", "cherry"}

# fruits.discard("banana")
# fruits.remove("banana2")

# print(fruits)
# -------------------------------------------------------------

# 12. pop() :-
fruits = {"apple", "banana", "cherry"}

fruits.pop()

# print(fruits)
# -------------------------------------------------------------

# 13. del :-
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)
# -------------------------------------------------------------

# 14. clear() :-
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)
# -------------------------------------------------------------

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")