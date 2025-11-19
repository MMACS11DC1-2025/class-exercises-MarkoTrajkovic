from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    else:
        return "other"
    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

yellow_pixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            file.putpixel((x,y), (255, 255, 255))

file.save("output.png", "png")
