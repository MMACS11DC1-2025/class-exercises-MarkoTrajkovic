"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#my program will use data from the class and find the classes favourite sport and how popular it is in a percentage, and the total average
#of the classes favouite digits.

file = open(responses.csv)

print("What is your name?")
name = input()

for line in file:
    if name in line:
        users_fav = line.split(",")
        print("Hello, " + name + ". Your favourite sport is " + line[4] + ". Do you want to know the favourite of the class?")

