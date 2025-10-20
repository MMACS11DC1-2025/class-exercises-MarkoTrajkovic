"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""



import turtle
t = turtle.Turtle()

answer = input("Want to see a cool star pattern?")
size = int(input("How big do you want the stars to be?"))
x = int(input("Where do you want the stars to start? (x axis)"))
y = int(input("Where do you want the stars to start? (y axis)"))

while True:
	def stars():
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.right(-70)
		t.forward(size)
		t.right(140)
		t.forward(size)
		t.right(150)
		t.forward(size)
		t.right(140)
		t.forward(size)
		t.right(145)
		t.forward(size + 15)
		t.penup()
    
	stars();