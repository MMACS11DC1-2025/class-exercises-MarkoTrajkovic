from PIL import Image

image_green = Image.open("CS11/5.1/kid-green.jpg").load()
image_beach = Image.open("CS11/5.1/beach.jpg").load()

def is_green(r, g, b):
    if r < 25 and r >= 0 and g > 230 and g <= 255 and b < 25 and b >= 0:
        return True
    else:
        return False

def color(r, g, b):
    if r == 255 and g == 0 and b == 0:
        return "red"
    if r == 0 and g == 255 and b == 0:
        return "green"
    if r == 0 and g == 0 and b == 255:
        return "blue"
    if r == 255 and g == 255 and b == 255:
        return "white"
    if r == 0 and g == 0 and b == 0:
        return "black"
    if r == 255 and g == 255 and b == 0:
        return "yellow"
    if r == 255 and g == 0 and b == 255:
        return "magenta"