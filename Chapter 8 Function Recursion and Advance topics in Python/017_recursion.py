'''
Recursion
Recursion is a programming technique in which a function calls itself directly or indirectly to solve a problem.

In other words: A big problem is broken into smaller subproblems of the same type, Until a base case (stopping condition) is reached.

Essential Parts of Recursion
Base Case → The condition where the function stops calling itself. (Prevents infinite loop) Recursive Case → The part where the function calls itself with a smaller/simpler input.
'''

# Recursive code for getting nth term of fibonacci series:

def fibo(n):
  if n == 0: # base case
      return 0
  if n == 1: # base case
     return 1
 # recursive case
  return fibo(n-1) + fibo(n-2)

print(fibo(7))

# Factorial

def factorial(n):
    if n == 0:   # base case
        return 1
    return n * factorial(n-1)

print(factorial(5))


# Sorting A List Using Recursion

def recursive_sort(L):
  if L == [ ]: # Base Case
     return L

  # Store minimum element of list in variable `mini`.
  mini = min(L)
  L.remove(mini) # Removes `minimum element` from the list

  # Recursive Case
  return [mini] + recursive_sort(L)


print(recursive_sort([23,45,23,11,67,44,33]))
