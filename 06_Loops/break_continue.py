# break

# for i in range(1, 12): 
#     print("5 x", i, "=", 5 * i) # printing the multiplication table of 5
#     if i == 10: # if the value of i is equal to 10 then break the loop
#         break # break the loop when i is equal to 10

# print("Loop is broken when i is equal to 10") # printing the message when the loop is broken
# --------------------------------------------------------------

# continue

for i in range(1, 12):
    if i == 10: # if the value of i is equal to 10 then continue the loop
        print("skip the iteration") # printing the message when the loop is continued
        continue # continue the loop when i is equal to 10
    print("5 x", i, "=", 5 * i) # printing the multiplication table of 5
# --------------------------------------------------------------

# do while loop in python
# i = 0
# while True: 
#     print(i)
#     i = i + 1
#     if(i%100 == 0):
#         break