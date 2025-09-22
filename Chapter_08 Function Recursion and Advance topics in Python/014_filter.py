def check_even(number):
  return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# if an element passed to check_even() returns True, select it
even_numbers_iterator = filter(check_even, numbers)
print(even_numbers_iterator)     # Output: <filter object at 0x7715fbaec0d0>
 
 
# converting to list
print(list(even_numbers_iterator))      # Output: [2, 4, 6, 8, 10]

# using lambda function
print(list(filter(lambda num: num%2==0, numbers)))
# Output: [2, 4, 6, 8, 10]