# string functions 

# 1 - len()
# 1. len () function – This function returns the length of the strings. 

str = "Ayush"
print(len(str))

# 2 2. String.endswith("rry") – This function_ tells whether the variable string ends with 
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends 
# with rry. 

# variablename.function


a1 = str.endswith("h")
a_1 = str.startswith("A")
a_2 = str.startswith("a")
a2 = str.endswith("H")
print(a1)
print(a_1)
print(a2)
print(a_2)

# 3. string.count("c") – counts the total number of occurrences of any character. 

count1 = str.count("r") 
count2 = str.count("u") 
print(count1)  # Output: 0
print(count2)  # Output: 1

# 4 - capitalize - 1st letter capital 

str2 = 'ayush'
print(str2.capitalize())


# string fucntions can only prints new string they can't change the given string because Strings are immutable ....
 