# 7. Write a program to find out whether a given post is talking about 
# “Ayush” or not.

post = input("Enter your post :")

if("Ayush".lower() in post.lower() ):
    print("This post is talking about Ayush ")

else:
    print("This post is not talking about Ayush ")