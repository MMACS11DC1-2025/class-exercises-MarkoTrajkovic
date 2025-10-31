'''
my program will use data from the class to your name, favourite sport, and someone elses
favourite sport of your choice. Then, it will find how many other people like that sport
and respond to the user depending on how many people like the sport.
'''
#information from file
file = open("2.4/responses.csv")

#initializing variable for 3rd question
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

#asks for new name
print("Who would you like to know their favourite sport?")
answer = input().lower()
file = open("2.4/responses.csv")

#Tells the new persons favourite sports to watch
for line in file:
    user_fav = line.split(",")
    if answer in line.lower():
        file = open("2.4/responses.csv")
        print(user_fav[1] + "'s favourite sport to watch is " + user_fav[6] + ".")
        break

#asks you if you would like to know how many people like to watch or play sport from the new person
print("Do you know how many people also like to watch and/or play that?")
answer2 = input().lower()

#if the answer is yes, will add 1 to a tally when the sport comes up in any line from the file
for line in file:
    if answer2 == "yes":
        file = open("2.4/responses.csv")
        if str(user_fav[6]) in line:
            similarsport += 1
#if answer is no, respond approprietly and stop the loop
    elif answer2 == "no":
        print("Oh. Ok.")
        break
#if answer is not yes or know, respond approprietly and stop the loop
    else:
        print("Sorry, im not sure what you mean.")
        break

#only if the answer is yes, the program will tell you how many instances of the sport shows up in the dataset.
if answer2 == "yes":
    print("Exactly " + str(similarsport) + " people like to watch and/or play " + user_fav[6] + "!")
#if the sport appears more than 5 times, it will respond appropriely
    if similarsport >= 5:
        print("Wow! Thats a popular sport!")
#if the sport appears less than 5 times, it will respond appropriely
    elif similarsport < 5:
        print("Not a very popular sport. " + answer + " likes a niche sport!")
        
            

    





    

