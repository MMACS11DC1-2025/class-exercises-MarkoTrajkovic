from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    elif r > 107 and g < 47 and b < 35:
        return "red"
    elif r < 95 and g < 148 and b > 95:
        return "blue"
    elif r < 66 and g > 21 and b < 42:
        return "green"
    elif r < 209 and g < 24 and b < 171:
        return "purple"
    
    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

yellow_pixels = []
red_p = []
blue_p = []
green_p = []
purple_p = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "red":
            red_p.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "blue":
            blue_p.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "green":
            green_p.append(jb_image[x,y])
        if colour(pixel_r, pixel_g, pixel_b) == "purple":
            purple_p.append(jb_image[x,y])

num_yellow = len(yellow_pixels)
total_pixels = width*height
yellow_ratio = num_yellow / total_pixels
yellow_percent = yellow_ratio * 100
output = "There are {:.2f}% yellow pixels".format(yellow_percent)
print(output)

num_red = len(red_p)
red_ratio = num_red / total_pixels
red_percent = red_ratio * 100
output_red = "There are {:.2f}% red pixels".format(red_percent)
print(output_red)

num_blue = len(blue_p)
blue_ratio = num_blue / total_pixels
blue_percent = blue_ratio * 100
output_blue = "There are {:.2f}% blue pixels".format(blue_percent)
print(output_blue)

num_green = len(green_p)
green_ratio = num_green / total_pixels
green_percent = green_ratio * 100
output_green = "There are {:.2f}% green pixels".format(green_percent)
print(output_green)

num_purple = len(purple_p)
purple_ratio = num_purple / total_pixels
purple_percent = purple_ratio * 100
output_purple = "There are {:.2f}% purple pixels".format(purple_percent)
print(output_purple)

file.save("output.png", "png")
