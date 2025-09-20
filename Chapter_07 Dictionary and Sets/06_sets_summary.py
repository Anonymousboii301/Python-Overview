


# In Python, a set is a built-in data type that stores unordered, unique elements. Sets are great for removing duplicates and performing operations like union, intersection, and difference.

# Creating a Set
# You can create a set using curly braces {} or the set() function.



# Using curly braces
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Using set() function
another_set = set([1, 2, 2, 3])
print(another_set)  # Output: {1, 2, 3}

# Key Characteristics
# Unordered: The elements do not have a specific order.
# Unique: No duplicate elements are allowed.
# Basic Operations
# Here are some common set operations:

# Adding Elements


my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing Elements


my_set.remove(3)  # Raises an error if the element is not found
print(my_set)  # Output: {1, 2, 4, 5}

my_set.discard(10)  # Does not raise an error if the element is not found
# Checking Membership


print(2 in my_set)   # Output: True
print(10 in my_set)  # Output: False
# Set Operations
# Python sets support several useful mathematical operations:

# Union (| or union())
# Combines elements from both sets.


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
# Intersection (& or intersection())
# Finds common elements in both sets.


print(set1 & set2)  # Output: {3}
print(set1.intersection(set2))  # Output: {3}
# Difference (- or difference())
# Finds elements in one set but not in the other.



print(set1 - set2)  # Output: {1, 2}
print(set1.difference(set2))  # Output: {1, 2}
# Symmetric Difference (^ or symmetric_difference())
# Finds elements in either set, but not in both.


print(set1 ^ set2)  # Output: {1, 2, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}
# Useful Set Methods
# Method	Description
# add(element)	Adds an element to the set
# remove(element)	Removes an element, raises KeyError if missing
# discard(element)	Removes an element if present, no error if not
# pop()	Removes and returns an arbitrary element
# clear()	Removes all elements from the set
# copy()	Returns a shallow copy of the set
# isdisjoint(other_set)	Checks if sets have no elements in common
# issubset(other_set)	Checks if the set is a subset of another
# issuperset(other_set)	Checks if the set is a superset of another
# Example


fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'banana', 'cherry', 'orange', 'apple'}

# Check for subset
citrus = {"orange"}
print(citrus.issubset(fruits))  # Output: True
# Let me know if you need more details or examples!




# 
# # Here are the common methods for Python sets, along with explanations and examples:

# 1. add()
# # Adds an element to the set. If the element already exists, it won't be added again.



my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
# 2. remove()
# # Removes a specified element from the set. Raises a KeyError if the element is not found.



my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# my_set.remove(5)  # Raises KeyError because 5 is not in the set
# 3. discard()
# # Removes a specified element from the set without raising an error if the element is not found.


my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

my_set.discard(5)  # No error, even though 5 is not in the set
# 4. pop()
# # Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.


my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: (any one of 1, 2, or 3)
print(my_set)   # Output: Remaining elements
# 5. clear()
# Removes all elements from the set, making it an empty set.

my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
# 6. union() or |
# Returns a new set with all elements from both sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5}
# 7. intersection() or &
# Returns a new set with only the elements common to both sets.



set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}
# 8. difference() or -
# Returns a new set with elements in the first set but not in the second.



set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}
# 9. symmetric_difference() or ^
# Returns a new set with elements in either set, but not in both.


set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}
# 10. update() or |=
# Updates the set with elements from another set or iterable (in-place union).


set1 = {1, 2}
set2 = {2, 3}
set1.update(set2)
print(set1)  # Output: {1, 2, 3}
# 11. intersection_update() or &=
# # Updates the set with elements common to both sets (in-place intersection).



set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}
# 12. difference_update() or -=
# Removes elements found in another set (in-place difference).



set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}
# 13. symmetric_difference_update() or ^=
# # Updates the set to keep only elements found in either set, but not in both (in-place symmetric difference).



set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 4}
# 14. issubset()
# Checks if all elements of the set are in another set.


set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
# 15. issuperset()
# Checks if the set contains all elements of another set.



set1 = {1, 2, 3}
set2 = {2, 3}
print(set1.issuperset(set2))  # Output: True
# 16. isdisjoint()
# Checks if two sets have no elements in common.



set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True
# 17. copy()
# Returns a shallow copy of the set.

original = {1, 2, 3}
copy_set = original.copy()
print(copy_set)  # Output: {1, 2, 3}
# These methods make Python sets versatile and powerful for various operations involving unique elements. If you have any specific questions about these methods, feel free to ask!





# 1. add()
# # Adds an element to the set. If the element already exists, it won't be added again.



my_set = {1, 2, 3}
my_set.add(4)  # Adds 4
print(my_set)  # Output: {1, 2, 3, 4}
# 2. remove()
# # Removes a specified element from the set. Raises a KeyError if the element is not found.



my_set = {1, 2, 3}
my_set.remove(2)  # Removes 2
print(my_set)  # Output: {1, 3}

# my_set.remove(5)  # Raises KeyError if element not found
# 3. discard()
# # Removes a specified element from the set without raising an error if the element is not found.
# 


my_set = {1, 2, 3}
my_set.discard(3)  # Removes 3
print(my_set)  # Output: {1, 2}

my_set.discard(5)  # No error even if 5 is not in the set
# 4. pop()
# # Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.


my_set = {1, 2, 3}
element = my_set.pop()  # Removes and returns an arbitrary element
print(element)  # Output: (any of the set's elements)
print(my_set)   # Remaining elements
# 5. clear()
# Removes all elements from the set, making it an empty set.



my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()
# 6. union() or |
# # Returns a new set containing all elements from both sets (combines sets).


set1 = {1, 2}
set2 = {2, 3}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3}

# Or using the | operator
result = set1 | set2
print(result)  # Output: {1, 2, 3}
# 7. intersection() or &
# Returns a new set containing only the elements common to both sets.



set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)  # Output: {2, 3}

# Or using the & operator
result = set1 & set2
print(result)  # Output: {2, 3}
# 8. difference() or -
# # Returns a new set containing elements that are in the first set but not in the second.


set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.difference(set2)
print(result)  # Output: {1}

# Or using the - operator
result = set1 - set2
print(result)  # Output: {1}
# 9. symmetric_difference() or ^
# # Returns a new set containing elements that are in either set, but not in both.



set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 4}

# Or using the ^ operator
result = set1 ^ set2
print(result)  # Output: {1, 4}
# 10. issubset()
# Checks if all elements of the set are in another set.



set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
# 11. issuperset()
# Checks if the set contains all elements of another set.



set1 = {1, 2, 3}
set2 = {2, 3}
print(set1.issuperset(set2))  # Output: True
# 12. isdisjoint()
# Checks if two sets have no elements in common.


set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True

# These methods are frequently used for manipulating sets and performing operations like combining, comparing, and updating sets. Understanding these will help you with most set-related tasks in Python.






