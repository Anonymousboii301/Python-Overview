# Example 1: 

try:
  print(5//0)

except ZeroDivisionError:
  print("Can't divide by zero")
else:
  print("This line is only gets executed when there is no exception")
finally:
  print('This line is always executed')

# Output 

'''
Can't divide by zero
This is always executed 
'''




# Example 2: 

try:
  print(5//2)

except ZeroDivisionError:
  print("Can't divide by zero")
else:
  print("This line is only gets executed when there is no exception")
finally:
  print('This line is always executed')


# Output
'''
2
This line is only gets executed when there is no exception
This is always executed
'''