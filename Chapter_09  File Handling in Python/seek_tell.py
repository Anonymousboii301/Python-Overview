# For this case assume the 'example.txt' contains the following line:
# Code is like humor. When you have to explain it, it’s bad.

f = open("ex_for_seek_tell.txt", "r")

# Second parameter is by default 0 (beginning of file).
# This moves the file pointer to the 20th index (starting from 0).
f.seek(20)

# Prints current position of the file pointer
print(f.tell())

# Reads from the 20th position until the end of line
print(f.readline())

f.close()

# Output
'''
20
When you have to explain it, it’s bad.
'''
