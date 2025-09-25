
# Example 1:
try:
  print(5/0)
  
except IndexError:
  print("Index Out of Bound.")
except ZeroDivisionError:
  print("Denominator cannot be 0.")
except:
  print("Some other exception occurred")


# Output
'''
Denominator cannot be 0.
'''




# Example 2: 


try:
  print(l)

except IndexError:
  print("Index Out of Bound.")
except ZeroDivisionError:
  print("Denominator cannot be 0.")


 # you can write the following line instead of just writing except
 # to view the error message associated with the Exception

except Exception as e:
  print(e)


# Output
'''
name 'l' is not defined
'''