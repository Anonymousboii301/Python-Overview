# In Python, lists and tuples are both data structures that are used to store collections of items. They have some similarities but differ in a few key ways. Here’s a detailed comparison:

# 1. List

# Definition: A list is an ordered collection of items that is mutable, meaning its elements can be changed after it is created.
# Syntax: Lists are defined using square brackets [].
# Example:

my_list = [1, 2, 3, "apple", 4.5]
# Characteristics:



# Mutable: Elements can be added, removed, or changed.

my_list[0] = 100  # Modifying the first element
print(my_list)    # Output: [100, 2, 3, "apple", 4.5]

# Dynamic: You can add or remove items using methods like .append(), .insert(), .pop().

my_list.append("banana")  # Adding an item
print(my_list)            # Output: [100, 2, 3, "apple", 4.5, "banana"]

# Heterogeneous: Can contain items of different types (integers, strings, floats, etc.).


# 2. Tuple

# Definition: A tuple is an ordered collection of items that is immutable, meaning its elements cannot be changed after it is created.
# Syntax: Tuples are defined using parentheses ().
# Example:

my_tuple = (1, 2, 3, "apple", 4.5)
# Characteristics:


# Immutable: Once a tuple is created, its elements cannot be modified.

# my_tuple[0] = 100  # This would raise a TypeError

# Fixed Size: The size of a tuple is fixed after creation.


# Heterogeneous: Can contain items of different types just like lists.

# Faster: Accessing elements in a tuple can be slightly faster than in a list due to its immutability.
''' comparison Table

Feature	   List	  Tuple
Syntax	     []	   ()
Mutability	Mutable (can change)	Immutable (cannot change)
Methods	Many methods (e.g., append, pop)	Limited methods (e.g., count, index)
Performance	Slower (due to mutability)	Faster (due to immutability)
Use Case	When you need a dynamic collection	When you need a fixed, unchangeable collection   '''
# Example Usage


# List Example
fruits_list = ["apple", "banana", "cherry"]
fruits_list.append("orange")  # Adding an item
print(fruits_list)            # Output: ['apple', 'banana', 'cherry', 'orange']

# Tuple Example
fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple.append("orange")  # This would raise an AttributeError
print(fruits_tuple)              # Output: ('apple', 'banana', 'cherry')


# When to Use Lists and Tuples
# Use a List when you need a collection of items that can change over time (e.g., a list of user inputs).
# Use a Tuple when you need a collection of items that should remain constant (e.g., coordinates of a point).
# Let me know if you need more details or examples!


