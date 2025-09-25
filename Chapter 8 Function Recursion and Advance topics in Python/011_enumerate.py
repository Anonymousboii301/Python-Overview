l1 = ["eat", "sleep", "repeat"]
s1 = "code"


obj1 = enumerate(l1)         # creating enumerate objects
obj2 = enumerate(s1)

print ("Return type:", type(obj1))     # Return type: <class 'enumerate'>
print (list(enumerate(l1)))          # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]


# changing start index to 2 from 0
print (list(enumerate(s1, 2)))        # [(2, 'c'), (3, 'o'), (4, 'd'), (5, 'e')]