import time
from PIL import Image
t0 = time.time()
def colour(r, g, b):
    if r >= 128 and g >= 128 and b >= 128:
        return "light"
    else:
        return "dark"
    
    
file = Image.open("5.1/jelly_beans.jpg")
image = file.load()

width = file.width
height = file.height

dark_pixels = []
light_pixels = []

for x in range(width):
    for y in range(height):
        pixel_r = image[x,y][0]
        pixel_g = image[x,y][1]
        pixel_b = image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "dark":
            dark_pixels.append(image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "light":
            light_pixels.append(image[x,y])



num_light = len(light_pixels)
total_pixels = width*height
light_ratio = num_light / total_pixels
light_percent = light_ratio * 100
output_light = "There are {:.2f}% light pixels".format(light_percent)
print(output_light)

num_dark = len(dark_pixels)
dark_ratio = num_dark / total_pixels
dark_percent = dark_ratio * 100
output_dark = "There are {:.2f}% dark pixels".format(dark_percent)
print(output_dark)

file.save("output.png", "png")

t3 = time.time()

total_time = t3 - t0

timings = "It took {:.2f} seconds to run all of the code.".format(total_time)
print(timings)