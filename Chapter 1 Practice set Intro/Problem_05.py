# Label the program written in problem 4 with comments. 

import os

# List files and directories in the current directory
contents = os.listdir()
print(contents)

# List files and directories in a specified path
path = '/'
contents = os.listdir(path)
print(contents)
