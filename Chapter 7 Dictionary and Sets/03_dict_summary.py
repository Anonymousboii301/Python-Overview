
#  source - https://chatgpt.com/share/67348e7d-e8a0-8000-a13d-93abcce54245

In Python, a dictionary is a data structure that stores data in key-value pairs. Dictionaries are mutable, unordered, and can hold data of different types.

Creating a Dictionary
You can create a dictionary using curly braces {} or the built-in dict() function.

python
Copy code
# Using curly braces
my_dict = {
    "name": "Bruce Wayne",
    "age": 35,
    "city": "Gotham"
}

# Using dict() function
another_dict = dict(id=101, title="Hero", alias="BATMAN")
Accessing Values
You can access the value associated with a key using square brackets [] or the get() method.

python
Copy code
print(my_dict["name"])  # Output: Bruce Wayne
print(my_dict.get("city"))  # Output: Gotham

# Using .get() method avoids KeyError
print(my_dict.get("job", "Not specified"))  # Output: Not specified
Adding and Updating Elements
You can add a new key-value pair or update an existing one.

python
Copy code
# Adding a new key-value pair
my_dict["occupation"] = "Vigilante"

# Updating an existing key
my_dict["age"] = 36
print(my_dict)  # {'name': 'Bruce Wayne', 'age': 36, 'city': 'Gotham', 'occupation': 'Vigilante'}
Removing Elements
Python provides several methods to remove items from a dictionary.

python
Copy code
# Using pop() method
my_dict.pop("city")  # Removes 'city'

# Using del keyword
del my_dict["occupation"]  # Removes 'occupation'

# Using popitem() method (removes the last inserted key-value pair)
my_dict.popitem()
Dictionary Methods
Here are some useful methods for dictionaries:

Method	Description
keys()	Returns a view object of dictionary keys.
values()	Returns a view object of dictionary values.
items()	Returns a view object of dictionary key-value pairs.
clear()	Removes all elements from the dictionary.
update()	Updates the dictionary with another dictionary's items.
Example:

python
Copy code
# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Getting all keys
print(my_dict.keys())  # dict_keys(['name', 'age'])

# Getting all values
print(my_dict.values())  # dict_values(['Bruce Wayne', 36])
Dictionary Comprehension
You can use dictionary comprehensions to create dictionaries dynamically.

python
Copy code
# Example: Squares of numbers
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Nested Dictionaries
You can create dictionaries inside dictionaries.

python
Copy code
# Example: Nested dictionary
batman_profile = {
    "identity": {"name": "Bruce Wayne", "alias": "Batman"},
    "gear": {"vehicle": "Batmobile", "weapon": "Batarang"}
}

print(batman_profile["identity"]["name"])  # Output: Bruce Wayne
Dictionaries are powerful and flexible, making them one of the most commonly used data structures in Python.




# 1. dict.get(key, default=None)
# Description: Returns the value of the specified key. If the key does not exist, it returns the specified default value (None if not provided).
# Example:

batman = {"name": "Bruce Wayne", "age": 35}
print(batman.get("name"))  # Output: Bruce Wayne
print(batman.get("city", "Gotham"))  # Output: Gotham



# 2. dict.keys()
# Description: Returns a view object that displays a list of all the keys in the dictionary.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
print(batman.keys())  # Output: dict_keys(['name', 'age'])


# 3. dict.values()
# Description: Returns a view object that displays a list of all the values in the dictionary.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
print(batman.values())  # Output: dict_values(['Bruce Wayne', 35])


# 4. dict.items()
# Description: Returns a view object that displays a list of dictionary's key-value tuple pairs.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
print(batman.items())  # Output: dict_items([('name', 'Bruce Wayne'), ('age', 35)])



# 5. dict.update([other])
# Description: Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
# Example:
batman = {"name": "Bruce Wayne"}
batman.update({"age": 35, "city": "Gotham"})
print(batman)  # Output: {'name': 'Bruce Wayne', 'age': 35, 'city': 'Gotham'}



# 6. dict.pop(key, default)
# Description: Removes the specified key and returns the corresponding value. If the key does not exist, it returns the specified default value.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
age = batman.pop("age")
print(age)  # Output: 35
print(batman)  # Output: {'name': 'Bruce Wayne'}



# 7. dict.popitem()
# Description: Removes and returns the last inserted key-value pair as a tuple. Raises KeyError if the dictionary is empty.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
last_item = batman.popitem()
print(last_item)  # Output: ('age', 35)
print(batman)  # Output: {'name': 'Bruce Wayne'}



# 8. dict.clear()
# Description: Removes all elements from the dictionary, leaving it empty.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
batman.clear()
print(batman)  # Output: {}



# 9. dict.copy()
# Description: Returns a shallow copy of the dictionary.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
batman_copy = batman.copy()
print(batman_copy)  # Output: {'name': 'Bruce Wayne', 'age': 35}


# 10. dict.fromkeys(iterable, value=None)
# Description: Creates a new dictionary with keys from the given iterable and values set to the specified value.
# Example:
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}




# 11. dict.setdefault(key, default=None)
# Description: Returns the value of a key if it is in the dictionary. If not, it inserts the key with the specified default value.
# Example:
batman = {"name": "Bruce Wayne"}
city = batman.setdefault("city", "Gotham")
print(city)  # Output: Gotham
print(batman)  # Output: {'name': 'Bruce Wayne', 'city': 'Gotham'}




# 12. len(dict)
# Description: Returns the number of key-value pairs in the dictionary.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
print(len(batman))  # Output: 2



# 13. in operator
# Description: Checks if a key exists in the dictionary.
# Example:
batman = {"name": "Bruce Wayne", "age": 35}
print("name" in batman)  # Output: True
print("city" in batman)  # Output: False
# These methods provide powerful ways to manipulate and interact with dictionaries in Python, making them a versatile and essential data structure in programming.