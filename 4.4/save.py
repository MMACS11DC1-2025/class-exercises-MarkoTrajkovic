import turtle

turt = turtle.Turtle()

size = int(input("What size is the starting fractal?"))


while size >= 0:
  def shape(size):
    turt.goto(0,0)
    turt.pendown()
    turt.circle(20+size)
    turt.forward(50+size)
    turt.left(40)
    turt.forward(20+size)
    if size <= 0:
      return 0
  shape(size)
  size -= 1