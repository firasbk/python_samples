blog_posts = ["","the 10 coolest functions in python","","how to make http requests in python","A tutorial about data types"]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

myString = "this is a string"
print("--------------")
for char in myString:
    print(char)

print("--------------")


blog_posts = {"python":["the 10 coolest functions in python","how to make http requests in python","A tutorial about data types"],"javascript":["how to make http requests in jabascript","A tutorial about javascripts"]}

for category in blog_posts:
    print("Posts about: ",category)
    for post in blog_posts[category]:
        print("The post is: ", post)
    print("----------------")

import random
colors = ["red","blue","black","white","violet","green","brown","grey"]

for i in range(0,2):
    number = random.randint(0,7)
    guess = colors[number]
    predicted = input("Enter a color to guess: ")
    if predicted == guess:
        print("BINGO: you guess the color", guess )
        break
    else:
        print("the color was ", guess)
        print("your color was: ", predicted)
        print ("try Again")

print("--------------")
names=[]
for x in range(0,7):
    name = input("please enter a name: ")
    names.append(name)

print("the names are: ", names)
ran = random.randint(0,7)
random_name = names[ran]
print ("random name is: ", random_name)
