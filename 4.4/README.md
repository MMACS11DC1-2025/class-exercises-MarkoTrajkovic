PROGRAM FUNCTION:
My program uses user input to draw a pattern from the middle of the screen(0,0). The user will be asked for a size(very small, small, medium, big, very big), and the output will be
assigned to a number, which is the size of the pattern. It will do the same with a color, assigning the list to a hex code and substituting the color. When the pattern is done, it
with display how many times the function has recursed by tracking a variable called count at the top of the function, so whenever the function is recursed the count will add 1 to itself.

METHOD I USED:
I first initilazed the variables i would need: the size and color of the function, and the count of the recursions. Then I defined the function, and added the Turtle code tha simply draws
a circle then a scalene triangle, and moving back to the start position. I then added code that decreases the size of the shape by 0.75 every recursion, which would work towards a base case
which is coming up. I then increases the count by one, which would count the amount of recursions there would be. Lastly, i added a base case, which says that when the size reaches 0 (after
decreasing by 0.75 every recursion), it will print the amount recursions and return 0, exiting the loop. Outside of the base case but inside the function, i called the function so it would
repeat itself until the base case is met. The last thing i did was call the function outside of the function to kick off the first recursion after all the input from the user was collected.

TESTING + DOCUMENTATION:
I tested the size of the shape by running the code 5 times to see if the pattern got bigger every increase of the desired size. I did the same with the color, testing all 5 of the avilable
colors to see if they visually changed. I tested the number of recursions my setting size to a constant divisible by 10, and doing easy math to check if the function worked. Since the size
decreased by 0.75, there should be 1.25 more recurions than the size. I tested the size to be 30 and got
