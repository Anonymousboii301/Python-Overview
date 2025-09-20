name = 'Ayush'

print(name[0:4])           # Ayus
print(name[0:5])          # Ayush

print(name[1])    # y
print(name[0])    # A
print(name[-1])  # h


# -ve  indexing ke liye corresponding +ve me convert kar le

print(name[-4:-1]) # yus
print(name[1:4])   # yus 

print(name[:4])   # same as name[0:4] = Ayus
print(name[1:])   # same as name[1:5] = yush
print(name[1:5])  # ,,                = yush


# Slicing with skip value 
word1= '1234567890'

print(word1[1:9:3])
# word1 starts with 1 indexing and goes to 8  -  23456789
# take after every 3rd word aother skiped    - 258

print(word1[1:9:2])           # 2468



word2 = 'abcdefghijklmnopqrstuvwxyz'
print(word2[1:10:3])  # bcdefghij   # beh


# Other advanced slicing techniques: 
# Word = "amazing" 
# Word = [:7]  # word [0:7] – 'amazing' 
# Word = [0:]  # word [0:7] – 'amazing'