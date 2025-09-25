# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# 
# s = {18 , "18"}
# print(s , type(s))

s = set()
n1 = int(input())
s.add(n1)
n2 = input()
s.add(n2)

print(s)