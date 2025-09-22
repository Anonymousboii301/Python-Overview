"""
Generators in Python :-

A generator is a simpler way to create an iterator using the yield keyword.

- Instead of returning all results at once, it yields one value at a time.
- Very memory efficient for large sequences.
"""


# 1.
def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3




# 2.
def power(limit):
    x = 0
    while x<limit:
        yield x*x
        yield x*x*x
        x += 1
a = power(5)
print(next(a), next(a))        # 0 0
print(next(a), next(a))        # 1 1
print(next(a))                   # 4
print(next(a))                  # 8            
print(next(a), next(a))         # 9 27    
            

'''
Key Differences (Iterator vs Generator)
# 
| Feature        | Iterator                                   | Generator                                |
| -------------- | ------------------------------------------ | ---------------------------------------- |
| **Definition** | Object with `__iter__()` and `__next__()`  | Function with `yield` keyword            |
| **Creation**   | From `iter()` or custom class              | From generator function/expression       |
| **Syntax**     | Complex (class needed)                     | Simple (just use `yield`)                |
| **Memory**     | Stores all elements (unless lazy iterator) | Produces values lazily, memory-efficient |
| **Example**    | `it = iter([1,2,3])`                       | `def gen(): yield 1`                     |

'''

