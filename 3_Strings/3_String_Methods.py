a = "subhajit"
# print(len(a)) # print string lenth
# -----------------------------------------------------------------

# print(a.upper()) # print string in upper case
# -----------------------------------------------------------------

# print(a.lower()) # print string in lower case
# -----------------------------------------------------------------

# b = "subhajit !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
b = "!!!!!!!!subhajit !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
# print(b.rstrip("!")) # Removes exclamation marks /!  from the right side
# -----------------------------------------------------------------

# print(a.replace("subhajit", "i love you")) # print string the new string
# -----------------------------------------------------------------

# c =" hello now are you ok "
# print(c.strip()) # Replaces outer spaces

c ="############# hello now are you ok #######################"
# print(c.strip("#")) # Removes exclamation marks /! from both ends
# print(c.lstrip("#")) # Removes exclamation marks /! from left side
# print(c.rstrip("#")) # Removes exclamation marks /! from right side
# -----------------------------------------------------------------

d ="hello i try to learn python programing"
# print(d.split()) # Splits the string into a list of words using spaces
# -----------------------------------------------------------------

# blogHeading = "hello, and welcome to my world."
blogHeading = "hello, anD welcome To my woRld." # same but in this string some latter in upercase this poblem fix it 
# print(blogHeading.capitalize()) # Capitalizes only the very first letter of the string
# -----------------------------------------------------------------

txt = "banana"

# print(len(txt)) # 6
# print(txt.center(20)) # Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
# print(len(txt.center(20))) # 20
# ---------------------------------------------------------------------

text2 ="I love apples, apple are my favorite fruit"
# print(text2.count("apple")) # Return the number of times the value "apple" appears in the string
# ---------------------------------------------------------------------

txt3 = "Hello, welcome to my world."
# print(txt3.endswith(".")) # Check if the string ends with a punctuation sign (.); and this data returns in Boolean(True/False)
# print(txt3.endswith("my world.", 5, 11)) # Check if position 5 to 11 ends with the phrase "my world."
# print(txt3.endswith(("my world.", "castle."))) # Check if the string ends with either the phrase "world." or "castle."
# ---------------------------------------------------------------------

# Returns the position of the specified value, or -1 if it is not found.
txt4 = "she's name is suravi and i love him but she not love's me, because she loves somone"
# print(txt4.find("khelo")) # to help find the text in string and show which pogisan this showing like 11.

text = "Programming"

# print(text.find("g", 4)) # Find 'g' starting from index 4
# print(text.find("g", 4, 7)) # Find 'g' between index 4 and 6 (end index is excluded)
# print(text.find("z"))  # Search for 'z', which is not present in the string
# ---------------------------------------------------------------------

txt5 = "Hello, welcome to my world."
# print(txt5.index("to"))# Returns the index of the first occurrence of the specified value.
# print(txt5.index("1to")) # Raises a ValueError if the value is not found.

text = "Programming"

# print(text.index("g", 4)) # Find 'g' starting from index 4
# print(text.index("g", 4, 7)) # Find 'g' between index 4 and 6 (end index is excluded)
# ---------------------------------------------------------------------

txt6 = "Company12"
# print(txt6.isalnum()) # checks whether the string contains only letters(A-Z, a-z) and numbers(0-9). and this data show in True/False
# ---------------------------------------------------------------------

txt7 = "Company"
# print(txt7.isalpha()) # checks whether the string contains only letters(A-Z, a-z) and this data show in True/False
# ---------------------------------------------------------------------

txt8 = "company"
# print(txt8.islower()) # Check if all the characters in the text are in lower case and this data show in True/False
# ---------------------------------------------------------------------

txt9 = "Hello! Are you #1? \n"
# print(txt9.isprintable()) # Check if all the characters in the text are printable and this data show in True/False
# ---------------------------------------------------------------------

txt10 = "   "
# print(txt10.isspace()) # Check if all the characters in the text are whitespaces and this data show in True/False
# ---------------------------------------------------------------------

txt11 = "Hello, And Welcome To My World!"
# print(txt11.istitle()) # Check if each word start with an upper case letter and this data show in True/False
# ---------------------------------------------------------------------

txt12 = "THIS IS NOW!"
# print(txt12.isupper()) #Check if all the characters in the text are in upper case and this data show in True/False
# ---------------------------------------------------------------------

txt13 = "Hello, welcome to my world."
# print(txt13.startswith("Hello1")) # Check if the string starts with "Hello" and this data show in True/False
# print(txt13.startswith("wel", 7, 20)) # Check if position 7 to 20 starts with the characters "wel"
# print(txt13.startswith(("Hello", "Hi"))) # CCheck if the string starts with either "Hello" or "Hi"
# ---------------------------------------------------------------------

txt14 = "Hello My Name Is PETER"
# print(txt14.swapcase()) #Make the lower case letters upper case and the upper case letters lower case
# ---------------------------------------------------------------------

txt15 = "Welcome to my world"
# print(txt15.title()) #Make the first letter in each word upper case
# ---------------------------------------------------------------------



