file = open("2.4/responses.csv")


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