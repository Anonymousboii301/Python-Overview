'''
Linear Search and Binary Search
1. Linear Search
Definition

Linear Search is the simplest searching algorithm. It checks every element one by one until the desired element is found, or the list ends.

Steps-

Start from the first element.

Compare each element with the target.

If match found → return index.

If end reached without match → return "not found".

Example in Python
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index
    return -1          # not found

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # Output: 2
print(linear_search(arr, 99))  # Output: -1


'''
Works on unsorted or sorted lists.

Time Complexity: O(n) (worst case: check all elements).
'''

'''
2. Binary Search
Definition

Binary Search is a divide-and-conquer searching algorithm.It only works on a sorted array.It repeatedly divides the search interval in half.

Steps

Start with the middle element.
If target == middle → found.
If target < middle → search left half.
If target > middle → search right half.
Repeat until element is found or interval is empty.
Example in Python
'''


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2   # middle index
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1   # not found

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 30))  # Output: 2
print(binary_search(arr, 99))  # Output: -1


# An Iterative Code For Binary Search :


def binary_search(L, x):
    while L:  # Would repeat the process till list becomes empty.
        mid = len(L) // 2

        if L[mid] == x:
            return 'Element Found.'

        elif L[mid] > x:  # If `x` is less than middle element, then we'll check the left half of the list.
            L = L[:mid]

        elif L[mid] < x:  # If `x` is greater than middle element, then we'll check the right half of the list.
            L = L[mid+1:]
            
    # If we couldn't find the element and the list becomes empty.
    return 'Element Not Found.'

print(binary_search([10, 20, 30, 40, 50], 30))  # ✅ Element Found.
print(binary_search([10, 20, 30, 40, 50], 99))  # ❌ Element Not Found.



# Binary Search Using Recursion :


def recursive_binary_search(L, x):
    mid = len(L) // 2

    if not(L):  # Base case for if element not in list (ie. list becomes empty).
        return 'Element Not Found'

    elif L[mid] > x:    # Recursive Case (Checking the left part when `x` < middle element)
        return recursive_binary_search(L[:mid], x)

    elif L[mid] < x:  # Recursive Case (Checking the right part when `x` > middle element)
        return recursive_binary_search(L[mid+1:], x)

    return 'Element Found'  # Base case for element found in list.



print(recursive_binary_search([10, 20, 30, 40, 50], 40))  # ✅ Element Found
print(recursive_binary_search([10, 20, 30, 40, 50], 99))  # ❌ Element Not Found
