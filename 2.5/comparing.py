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

#finds name of user
print("What is your name? Include proper capitalization.")
name = input()

#matches name with dataset and tells favourite sport
for line in file:
    if name in line:
        user_fav = line.split(",")
        print("Hello, " + name + ". Your favourite sport to play is " + user_fav[5] + ". Who would you like to know their favourite sport to watch?")
        answer = input()

#matches other persons name with data set, tells favourite sport to watch
for line in file:
    if answer in line:
        person_fav = line.split(",")
        print(person_fav[1] + "'s favourite sport to watch is " + person_fav[6] + ".")

    
    

