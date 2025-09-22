# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time.
def rem( l , word):
    for item in l:
        l.remove(word)
        return l

l = ["ayush" , "rohan" , "sakshi" ,"anjali" , "paras"  ]

print(rem(l,"sakshi"))













def rem( l , word):
    n = []
    for item in l :
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["ayush" , "rohan" , "sakshi", "an" ,"anjali" , "paras"]

print(rem(l,"an"))