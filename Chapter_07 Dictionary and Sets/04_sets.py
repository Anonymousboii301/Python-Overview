'''
SETS IN PYTHON. 
Set is a collection of non-repetitive elements. 
s = set()           
# no repetition allowed! 
s.add(1) 
s.add(2)           
# or set ={1,2} 
20 
If you are a programming beginner without much knowledge of mathematical 
operations on sets, you can simply look at sets in python as data types containing 
unique values.
'''

'''
In Python, a set is a built-in data type that stores unordered, unique el
ements. Sets are great for removing duplicates and performing operations like union, intersection, and difference.'''


s = {1,2,3,4,5,}   # set
empty_set = set()
d = {}
print(type(s))
print(type(empty_set))   # set 
print(type(d))   # dict 

#  No element in set repeat twice 
set1 = {1,22,3,4,4,4,5,5,5,5,5,5,5,78}
print(set1)



'''
PROPERTIES OF SETS 
1. Sets are unordered => Element’s order doesn’t matter 
2. Sets are unindexed => Cannot access elements by index 
3. There is no way to change items in sets. 
4. Sets cannot contain duplicate values. 
'''
