# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]} 

# no indexing no hashable 
s1 = {1,2,3,3,3,3,3,2,[2,4]}
print(s1)


'''

No, you cannot have a list inside a set in Python. This is because sets in Python only allow immutable (hashable) elements, and lists are mutable (their contents can be changed), so they are not hashable.

Example:
python
Copy code
# This code will raise an error
s = {8, 7, 12, "Harry", [1, 2]}
Output:
bash
Copy code
TypeError: unhashable type: 'list'
Why this error?
Lists are mutable and can be changed, so their hash value can change. This conflicts with how sets work because sets use hash values to store and manage elements.
Sets require all elements to be hashable (immutable) because they use a hashing mechanism for quick lookup.
What can you do?
If you need a collection of values inside a set, you can use a tuple instead of a list, because tuples are immutable.

python
Copy code
s = {8, 7, 12, "Harry", (1, 2)}  # Using a tuple instead of a list
print(s)
Output:
arduino
Copy code
{8, 7, 12, 'Harry', (1, 2)}
In this case, (1, 2) is a tuple and is hashable, so it can be an element of the set.


'''