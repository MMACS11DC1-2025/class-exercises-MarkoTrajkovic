import turtle

turt = turtle.Turtle()
turt.speed(0)
size = int(input("What size is the starting fractal?"))



def shape(size):
  turt.goto(0,0)
  turt.pendown()
  turt.circle(20+size)
  turt.forward(50+size)
  turt.left(40)
  turt.forward(20+size)
  size -= 1
  if size <= 0:
    return 0
  shape(size)
shape(size)