from PIL import Image
import is_binarized
image_beach = Image.open("5.1/kid-green.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_beach[i,j][0]
        g = image_beach[i,j][1]
        b = image_beach[i,j][2]
        if is_binarized.is_light(r, g, b) == True:
            image_output.putpixel((i,j), (255, 255, 255))
        else:
            image_output.putpixel((i,j), (0, 0, 0))
image_output.save("output.png", "png")
        