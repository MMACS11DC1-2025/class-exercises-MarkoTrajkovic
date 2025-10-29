import turtle

#initializes turtle variable
turt = turtle.Turtle()
turt.speed(0)

#asks user for size of the shape. The higher size the bigger the pattern and more recursion
size = int(input("What size is the starting fractal?"))
direction = input("Where do you want the shape to start? top left or right, bottom left or right, or in the center?").lower()
x = {top left:-100, bottom left:-100, top right:100, bottom right:100, center:0}
y = {top left:80, bottom left:-80, top right:80, bottom right:-80, center:0}

#initializes count variable, important for printing total recursions
count = 0

#defines the function with parameters size and count.
def shape(size, count):
  #everytime the function runs, makes a circle and a scalene triangle that goes back to 0,0
  turt.goto(x,y)
  turt.pendown()
  turt.circle(20+size)
  turt.forward(50+size)
  turt.left(40)
  turt.forward(20+size)
  #size decreases, works towards base case
  size -= 0.75
  #count keeps track of amount of recursions
  count += 1
  #when the size gets to 0, it says how many recursions happened and breaks the loop
  if size <= 0:
    print("This function recursed " + str(count) + " times!")
    return 0
    
  #the function calls itself
  shape(size, count)
  
#initially calls the function to kick of the recursion
shape(size, count)