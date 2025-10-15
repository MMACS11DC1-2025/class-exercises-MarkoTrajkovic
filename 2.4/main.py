file = open("2.4/responses.csv")


import turtle
t = turtle.Turtle()

answer = input("Want to see a bunch of stars?")
while True:
	def staircase():
		t.pendown()
		t.right(-70)
		t.forward(200)
		t.right(140)
		t.forward(200)
		t.right(150)
		t.forward(200)
		t.right(140)
		t.forward(185)
		t.right(145)
		t.forward(200)
		t.penup()
	staircase();