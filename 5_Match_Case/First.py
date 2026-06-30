# x = (int(input("enter your number: ")))

# day = x
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
# ---------------------------------------------------------------------------------------

status = 404

match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:  # "This '_' (underscore) means 'else' or the default case."
        print("Unknown Status")