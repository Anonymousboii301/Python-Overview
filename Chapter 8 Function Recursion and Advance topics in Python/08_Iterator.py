

"""## Iterators and Generators in Python

### Iterator

In Python, an iterator is an object used to iterate over iterable objects such as lists, 
tuples, dictionaries, and sets. An object is called iterable if we can get an iterator from 
it or loop over it.

● iter()  function is used to create an iterator containing an iterable object.

● next()  function is used to call the next element in the iterable object.

"""

iter_list = iter(['I', 'Love', 'Python'])
print(next(iter_list))      # I
print(next(iter_list))      # Love
print(next(iter_list))      # Python

nums = [1, 2, 3]
it = iter(nums)      # create iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # ❌ StopIteration