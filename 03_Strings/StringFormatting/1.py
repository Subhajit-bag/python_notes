text = "Hey my name is {} , i am {} years old and comming frome {}"

name = "Subhajit"
age = 22
country = "INDIA"

# print(text.format(name, age, country)) # Hey my name is Subhajit , i am 22 years old and comming frome INDIA
# print(text.format( age, country, name)) # Hey my name is 22 , i am INDIA years old and comming frome Subhajit
# print(f"Hey my name is {name} , i am {age} years old and comming frome {country}") # in this part when you don't use the f so show data this type -> Hey my name is {name} , i am {age} years old and comming frome {country} <- that's way we're use f
# print(f"Hey my name is {{name}} , i am {{age}} years old and comming frome {{country}}") #  Hey my name is {name} , i am {age} years old and comming frome {country} 

# ------------------------------------------------------------------------------------------------------------

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.09999)) # The :.2f modifier automatically rounds the decimal number 49.09999 to exactly two decimal places.


price = 49.09999
txt2 = f"For only {price:.2f} dollars!"
print(txt2)

print((f"{2 * 30}"))
print(type(f"{2 * 30}"))
