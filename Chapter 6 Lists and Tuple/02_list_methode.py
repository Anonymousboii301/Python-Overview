# List methods - 
'''
In Python, a list method is a built-in function that can be called on a list
 object to perform a specific operation on the list. These methods allow you
 to manipulate, modify, or retrieve information from lists without needing to 
write additional code.

'''

friends = ["Apple" , 'banana' , 5 , 456.7 , "Ayush" , False , "Bruce wayne"]
print(friends)

friends.append("me")
print(friends)    # List changed here by append method 

l1 = [56,78,45,67,23,78,12,90,56,34,778,]

l1.sort()    # this sort the list in increasing order 
print(l1)


l1 = [56,78,45,67,23,78,12,90,56,34,778,]
l1.reverse()      # It just reverase the given list
print(l1)


l1 = [56,78,45,67,23,78,12,90,56,34,778,]
l1.insert(4 , 688888888)    # ( index , inserting number of item )   inserts in list 
print(l1)


l1 = [56,78,45,67,23,78,12,90,56,34,778,]
# l1.pop(5)   # 5th index element removed 
print(l1.pop(5))  # 5th index ki value prints  return value  
print(l1)


l1 = [56,78,45,67,23,78,12,90,56,34,778,]
l1.remove(78)   # (value)    - value removes from list
print(l1)



# Here is a list of commonly used methods for lists in Python:

# 1. append(item)
# Adds an item to the end of the list.

my_list = [1, 2, 3]
my_list.append(4)
# Result: [1, 2, 3, 4]

# 2. extend(iterable)
# Extends the list by appending elements from another iterable (e.g., another list).


my_list = [1, 2, 3]
my_list.extend([4, 5])
# Result: [1, 2, 3, 4, 5]

# 3. insert(index, item)
# Inserts an item at a specified index.

my_list = [1, 2, 3]
my_list.insert(1, 10)
# Result: [1, 10, 2, 3]


# 4. remove(item)
# Removes the first occurrence of an item.

my_list = [1, 2, 3, 2]
my_list.remove(2)
# Result: [1, 3, 2]

# 5. pop(index)
# Removes and returns the item at the specified index. If no index is provided, it removes the last item.

my_list = [1, 2, 3]
item = my_list.pop()
# Result: item = 3, my_list = [1, 2]

# 6. index(item, start, end)
# Returns the index of the first occurrence of an item. Optional start and end define a range.

my_list = [1, 2, 3, 2]
index = my_list.index(2)
# Result: index = 1

# 7. count(item)
# Returns the number of times an item appears in the list.

my_list = [1, 2, 2, 3]
count = my_list.count(2)
# Result: count = 2

# 8. sort(key=None, reverse=False)
# Sorts the list in ascending order. key is a function that extracts a comparison key from each list element, and reverse=True sorts in descending order.

my_list = [3, 1, 2]
my_list.sort()
# Result: [1, 2, 3]
my_list.sort(reverse=True)
# Result: [3, 2, 1]

# 9. reverse()
# Reverses the order of the list in place.

my_list = [1, 2, 3]
my_list.reverse()
# Result: [3, 2, 1]

# 10. copy()
# Returns a shallow copy of the list.

my_list = [1, 2, 3]
copied_list = my_list.copy()
# Result: copied_list = [1, 2, 3]

# 11. clear()
# Removes all items from the list.

my_list = [1, 2, 3]
my_list.clear()
# Result: []

# Examples of Usage

# Example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")   # ['apple', 'banana', 'cherry', 'orange']
fruits.remove("banana")   # ['apple', 'cherry', 'orange']
fruits.sort()             # ['apple', 'cherry', 'orange']
# These methods provide a versatile set of tools for working with lists in Python. If you have specific questions about any of these methods, feel free to ask!

# Here is a comprehensive list of Python's list methods and their descriptions:

# Python List Methods/Functions
'''
Method	                Description
append(item)	     Adds an item to the end of the list.
extend(iterable)	Extends the list by adding all items from the given iterable (e.g., another list).
insert(index, item)	Inserts an item at the specified index.
remove(item)	Removes the first occurrence of the specified item.
pop([index])	Removes and returns the item at the specified index (last item if index is not provided).
clear()	Removes all items from the list, resulting in an empty list.
index(item, [start, end])	Returns the index of the first occurrence of the specified item.
count(item)	Returns the number of occurrences of the specified item in the list.
sort(key=None, reverse=False)	Sorts the list in ascending order by default. Supports custom sorting via key.
reverse()	Reverses the elements of the list in place.
copy()	Returns a shallow copy of the list.
'''


 # Built-in Functions with Lists
# In addition to list methods, there are also built-in functions in Python that can be used with lists:
'''
Function	Description
len(list)	Returns the number of items in the list.
max(list)	Returns the maximum value in the list (if all items are comparable).
min(list)	Returns the minimum value in the list (if all items are comparable).
sum(list)	Returns the sum of all elements in the list (if they are numbers).
sorted(list)	Returns a new sorted list from the elements of any iterable.
list(iterable)	Creates a list from an iterable (e.g., tuple, set, string).
any(list)	Returns True if any element of the list is True.
all(list)	Returns True if all elements of the list are True.
enumerate(list)	Returns an enumerate object, providing an index and value.
filter(function, iterable)	Filters elements based on a function, returning a filtered list.
map(function, iterable)	Applies a function to all items and returns a mapped list.'''

# https://chatgpt.com/share/672f3a3a-0b34-8000-8e6e-ed09758c269c 
# source - chatgpt 