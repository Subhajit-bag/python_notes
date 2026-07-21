# a = int(input("Enter any value between 5 and 9: "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# *********************************************************

# ATM Withdrawal

# Account_balance = 5000

# a = int(input("Enter Withdrawal value: "))

# if a <= 0:
#     raise ValueError("Entry minimum value is 1")

# elif a > Account_balance:
#     raise ValueError("Insufficient Balance")

# else:
#     print("Withdrawal Successful")
#     print("Remaining balance:", Account_balance - a)
# *********************************************************

# Online Exam Marks Validation

# user_marks = int(input("Enter any value between 0 and 100: "))

# if (user_marks<0):
#     raise ValueError("Marks cannot be negative")
# elif(user_marks>100):
#     raise ValueError("Marks cannot be greater than 100")
# else:
#     print("Valid Marks")
#     print('''90+ → A
# 80-89 → B
# 70-79 → C
# 60-69 → D
# Belo 60 → F''')

#     if user_marks >= 90:
#         grade = "A"
#     elif user_marks >= 80:
#         grade = "B"
#     elif user_marks >= 70:
#         grade = "C"
#     elif user_marks >= 60:
#         grade = "D"
#     else:
#         grade = "F"

#     print(f"Your marks: {user_marks}")
#     print(f"Your grade: {grade}")
#     print(f"your number is : {user_marks} so your grade is {grade}")
# *********************************************************

# Password Validation

Password = input("Enter any value above 9 and use 0-9 digit: ")

if len(Password) < 8:
    raise ValueError("Password must be at least 8 characters long")

elif not any(char.isdigit() for char in Password):
    raise ValueError("Password must contain at least one digit")

else:
    print(f"Password Accepted and your password is {Password}")


