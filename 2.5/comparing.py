"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#my program will use data from the class to find others with the same favourite sport as you, and the total average of everyones
#favourite digit.

#information from file
file = open("2.4/responses.csv")

similarsport = 0

#finds name of user
print("What is your name?")
name = input().lower()

#matches name with dataset and tells favourite sport
for line in file:
    user_fav = line.split(",")
    person_fav = line.split(",")
    if name in line.lower():
        print("Hello, " + name + ". Your favourite sport to play is " + user_fav[5] + ".\n")
    else:
        continue

print("Who would you like to know their favourite sport?")
answer = input().lower()
file = open("2.4/responses.csv")
    
for line in file:
    user_fav = line.split(",")
    if answer in line.lower():
        file = open("2.4/responses.csv")
        print(user_fav[1] + "'s favourite sport to watch is " + user_fav[6] + ".")

print("Do you know how many people also like to watch or play that?")
answer2 = input().lower()
    
for line in file:
    if answer2 == "yes":
        file = open("2.4/responses.csv")
        if str(user_fav[6]) in line:
            similarsport += 1
print("Exactly " + str(similarsport) + " people like to watch and/or play " + user_fav[6] + "!")
#matches other persons name with data set, tells favourite sport to watch
if similarsport >= 5:
    print("Wow! Thats a popular sport!")
elif similarsport < 5:
    print("Not a very popular sport. " + answer + " likes a niche sport!")
        
            

    





    

