# Python has many useful string functions, each serving different purposes, depending on what you want to do. Here are some of the most commonly used and useful string functions in Python:

# 1. str.lower() / str.upper()
# Converts the string to lowercase or uppercase.
# Useful for case-insensitive comparisons or uniform formatting.

text = "Hello World"
print(text.lower())  # Output: "hello world"
print(text.upper())  # Output: "HELLO WORLD"


# 2. str.strip() / str.lstrip() / str.rstrip()
# Removes leading and trailing whitespace (or specified characters).
# Essential for cleaning up user input or removing unnecessary spaces.

text = "   Hello World   "
print(text.strip())  # Output: "Hello World"
print(text.lstrip()) # Output: "Hello World   "
print(text.rstrip()) # Output: "   Hello World"

# 3. str.replace(old, new)
# Replaces all occurrences of a substring with another substring.
# Useful for text manipulation or replacing certain words.

text = "Hello World"
print(text.replace("World", "Python"))  # Output: "Hello Python"


# 4. str.split(delimiter)
# Splits the string into a list of substrings based on the specified delimiter.
# Helpful for parsing CSV data, breaking up sentences, etc.


text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']


# 5. str.join(iterable)
# Joins a list of strings into a single string, with each element separated by the string it was called on.
# Ideal for reassembling lists into a single string.

fruits = ["apple", "banana", "cherry"]
print("//".join(fruits))  # Output: "apple, banana, cherry"


# 6. str.find(substring)
# Returns the index of the first occurrence of the specified substring (or -1 if not found).
# Useful for locating substrings or checking if a substring exists.

text = "Hello World"
print(text.find("World"))  # Output: 6
print(text.find("Python")) # Output: -1


# 7. str.startswith(prefix) / str.endswith(suffix)
# Checks if the string starts or ends with a specified prefix or suffix.
# Handy for filtering text or validating inputs.


text = "Hello World"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("World"))    # Output: True


# 8. str.isdigit() / str.isalpha() / str.isalnum()
# Checks if the string is numeric (isdigit), alphabetic (isalpha), or alphanumeric (isalnum).
# Useful for validating inputs (e.g., checking if input is a number).


text = "123"
print(text.isdigit())  # Output: True
text = "Hello123"
print(text.isalnum())  # Output: True

# 9. str.format()
# Allows inserting variables or expressions into a string, using curly braces {} as placeholders.
# Useful for creating dynamic strings.


name = "Batman"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: "My name is Batman and I am 30 years old."

# 10. str.count(substring)
# Counts the occurrences of a substring in the string.
# Useful for analyzing text or checking word frequency.


text = "banana"
print(text.count("a"))  # Output: 3
# Each of these functions can help you manage and manipulate strings more effectively, making your Python code cleaner and more efficient.








# Python has a wide variety of built-in string methods to perform operations on strings. Here’s a comprehensive list of all the main string functions:

# 1- Basic Formatting and Case Conversion


# a - str.capitalize()

# Converts the first character to uppercase, all others to lowercase.
# Example: "hello world".capitalize() → "Hello world"


# b - str.title()

# Capitalizes the first letter of each word in the string.
# Example: "hello world".title() → "Hello World"


# c str.upper()

# Converts all characters to uppercase.
# Example: "hello world".upper() → "HELLO WORLD"


# d - str.lower()

# Converts all characters to lowercase.
# Example: "HELLO WORLD".lower() → "hello world"


#E - str.swapcase()

# Converts uppercase to lowercase and vice versa.
# Example: "Hello World".swapcase() → "hELLO wORLD"


# f - str.casefold()

# Converts string to lowercase, similar to lower(), but more aggressive in language support.
# Example: "HELLO".casefold() → "hello"











# 2 - Whitespace and Character Stripping
# a - str.strip([chars])

# Removes leading and trailing whitespace (or specified characters).
# Example: " hello world ".strip() → "hello world"


# b - str.lstrip([chars])

# Removes leading whitespace (or specified characters).
# Example: " hello world".lstrip() → "hello world"

# c - str.rstrip([chars])

# Removes trailing whitespace (or specified characters).
# Example: "hello world ".rstrip() → "hello world"


# Search and Count


# str.find(sub[, start[, end]])

# Returns the index of the first occurrence of sub, or -1 if not found.
# Example: "hello world".find("world") → 6
# str.rfind(sub[, start[, end]])

# Returns the index of the last occurrence of sub, or -1 if not found.
# Example: "hello world".rfind("o") → 7
# str.index(sub[, start[, end]])

# Same as find(), but raises ValueError if sub is not found.
# Example: "hello world".index("world") → 6
# str.rindex(sub[, start[, end]])

# Same as rfind(), but raises ValueError if sub is not found.
# Example: "hello world".rindex("o") → 7
# str.count(sub[, start[, end]])

# Returns the number of non-overlapping occurrences of sub in the string.
# Example: "hello world".count("o") → 2





# Replacement
# str.replace(old, new[, count])
# Replaces all (or up to count) occurrences of old with new.
# Example: "hello world".replace("world", "Python") → "hello Python"









# Splitting and Joining
# str.split(sep=None, maxsplit=-1)

# Splits the string into a list of substrings based on sep.
# Example: "apple,banana,cherry".split(",") → ["apple", "banana", "cherry"]
# str.rsplit(sep=None, maxsplit=-1)

# Splits from the right, similar to split().
# Example: "apple,banana,cherry".rsplit(",", 1) → ["apple,banana", "cherry"]
# str.splitlines(keepends=False)

# Splits at line breaks, returning a list of lines.
# Example: "hello\nworld".splitlines() → ["hello", "world"]
# str.join(iterable)

# Joins elements of an iterable into a single string, separated by the string it was called on.
# Example: ", ".join(["apple", "banana", "cherry"]) → "apple, banana, cherry"





# Checking Properties
# str.startswith(prefix[, start[, end]])

# Returns True if the string starts with prefix.
# Example: "hello world".startswith("hello") → True
# str.endswith(suffix[, start[, end]])

# Returns True if the string ends with suffix.
# Example: "hello world".endswith("world") → True
# str.isalpha()

# Returns True if all characters are alphabetic.
# Example: "hello".isalpha() → True
# str.isdigit()

# Returns True if all characters are digits.
# Example: "12345".isdigit() → True
# str.isalnum()

# Returns True if all characters are alphanumeric.
# Example: "hello123".isalnum() → True
# str.isdecimal()

# Returns True if all characters are decimal characters.
# Example: "123".isdecimal() → True
# str.isnumeric()

# Returns True if all characters are numeric.
# Example: "123".isnumeric() → True
# str.isspace()

# Returns True if all characters are whitespace.
# Example: " ".isspace() → True
# str.islower()

# Returns True if all characters are lowercase.
# Example: "hello".islower() → True
# str.isupper()

# Returns True if all characters are uppercase.
# Example: "HELLO".isupper() → True
# str.istitle()

# Returns True if the string is in title case.
# Example: "Hello World".istitle() → True










# Alignment

# str.center(width[, fillchar])

# Centers the string in a field of the given width.
# Example: "hello".center(10, "-") → "--hello---"
# str.ljust(width[, fillchar])

# Left-justifies the string in a field of the given width.
# Example: "hello".ljust(10, "-") → "hello-----"
# str.rjust(width[, fillchar])

# Right-justifies the string in a field of the given width.
# Example: "hello".rjust(10, "-") → "-----hello"
# str.zfill(width)

# Pads the string with zeros on the left, up to the specified width.
# Example: "42".zfill(5) → "00042"












# Encoding and Formatting
# str.encode(encoding="utf-8", errors="strict")

# Encodes the string into bytes using the specified encoding.
# Example: "hello".encode("utf-8") → b'hello'
# str.format(*args, **kwargs)

# Formats the string using placeholders {}.
# Example: "Hello, {}".format("world") → "Hello, world"
# str.format_map(mapping)

# Similar to format(), but with a dictionary.
# Example: "{name}".format_map({"name": "Batman"}) → "Batman"




# String Translation and Removal
# str.translate(table)

# Returns a copy of the string where each character is mapped to a new character defined in a translation table.
# Example: "hello".translate(str.maketrans("h", "y")) → "yello"
# str.maketrans(x, y, z=None)

# Creates a translation table for translate(), mapping x to y and deleting characters in z.
# Example: str.maketrans("abc", "123")
# This list includes nearly every string method you’ll commonly use or encounter in Python, covering tasks from formatting to complex text processing.




