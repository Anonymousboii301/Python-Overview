a1 = 'He is a good but\nnot a bad boy' # \n new line
print(a1)

a2 =  "He is a good but a \"bad\"boy"   # " "
print(a2)

# \ t for tab 
# \'  for single quotes 
# \\  for backslash  


#  Here are the escape sequences in Python:






# """
# Escape Sequence	Description
# \\	Backslash (\)
# \'	Single quote (')
# \"	Double quote (")
# \n	Newline
# \t	Horizontal tab
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \v	Vertical tab
# \0	Null character
# \ooo	Octal value (e.g., \141 for 'a')
# \xhh	Hexadecimal value (e.g., \x61 for 'a')
# \N{name}	Unicode character by name
# \uhhhh	16-bit Unicode (e.g., \u03A9 for Ω)
# \Uhhhhhhhh	32-bit Unicode
# """
# These escape sequences are commonly used to insert special characters in strings and help with text formatting in Python. Let me know if you need more examples of how to use them!



#  Examples 

# Backslash
print("This is a backslash: \\")

# Single quote
print('It\'s a single quote inside single quotes.')

# Double quote
print("He said, \"Hello!\"")

# Newline
print("Hello\nWorld")

# Horizontal tab
print("Hello\tWorld")

# Carriage return
print("Hello\rWorld")  # 'Hello' is overwritten by 'World'

# Backspace
print("Helloo\b World")  # Removes the extra 'o'

# Form feed
print("Hello\fWorld")

# Vertical tab
print("Hello\vWorld")

# Null character
print("Hello\0World")  # Does not terminate the string but adds a null character

# Octal value
print("Octal example: \141")  # Output: 'a'

# Hexadecimal value
print("Hexadecimal example: \x61")  # Output: 'a'

# Unicode character by name
print("Unicode by name: \N{GREEK CAPITAL LETTER OMEGA}")  # Output: Ω

# 16-bit Unicode
print("16-bit Unicode: \u03A9")  # Output: Ω

# 32-bit Unicode
print("32-bit Unicode: \U0001F600")  # Output: 😀 (grinning face emoji)




