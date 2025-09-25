def square(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(square, numbers)    
print(result)        # Output: <map object at 0x7f722da129e8>
print(set(result))   # Output: {16, 1, 4, 9}


# using lambda function in map
print(list(map(lambda x: x*x, numbers))) # Output: [1, 4, 9, 16]


num1 = [1, 2, 3]
num2 = [10, 20, 40]


# add corresponding items from the num1 and num2 lists
result = map(lambda n1, n2: n1+n2, num1, num2)
print(tuple(result))        # Output: (11, 22, 43)