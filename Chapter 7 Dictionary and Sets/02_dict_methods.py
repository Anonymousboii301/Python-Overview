'''
DICTIONARY METHODS 
Consider the following dictionary. 
a={"name":"harry" 
"from":"india" 
"marks":[92,98,96]} 
• a.items(): Returns a list of (key,value)tuples. 
• a.keys(): Returns a list containing dictionary's keys. 
• a.update({"friends":}): Updates the dictionary with supplied key-value pairs. 
• a.get("name"): Returns the value of the specified keys (and value is returned 
eg."harry" is returned here).
'''

marks = {
    "Ayush" : 100,
    "Devansh" :  67,
    "anna" : 56,
    0 : "BAtman"

}



print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Ayush" : 23,'renu' : 12})  # mutuable 
print(marks)

print(marks.get('Ayush'))
print(marks.get('Huehuehue'))    # this print none 

# print(marks["Huehuehue"])      # this return error 
print(marks['Ayush'])

print(len(marks))

