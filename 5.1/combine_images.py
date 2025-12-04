from PIL import Image
import image_open

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_green[i,j][0]
        g = image_green[i,j][1]
        b = image_green[i,j][2]

        if image_open.is_green(r, g, b):
            beach_colour = image_beach[i,j]
            image_output.putpixel((i,j), beach_colour)

image_output.save("output.png", "png")
