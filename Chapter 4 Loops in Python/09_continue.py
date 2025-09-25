'''
THE CONTINUE STATEMENT 
‘continue’ is used to stop the current iteration of the loop and continue with the next 
one. It instructs the Program to “skip this iteration”. 
Example: 
for i in range(4): 
print("printing") 
if i == 2:   # if i is 2, the iteration is skipped  
continue 
print(i) 
'''
for i in range(100):
    if(i==3):
        continue    # skip this iteration right now 
    print(i)    # 3 not printed