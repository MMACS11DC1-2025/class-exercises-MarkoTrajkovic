from PIL import Image
import is_flag

image = Image.open("6.7/americanflag4.jpg").load()
image_output = Image.open("6.7/americanflag4.jpg")

width = image_output.width
height = image_output.height

blue_pixels = []
red_pixels = []
white_pixels = []
other_pixels = []

for i in range(width):
    for j in range(height):
        r = image[i,j][0]
        g = image[i,j][1]
        b = image[i,j][2]

        if is_flag.is_flag(r, g, b) == "blue":
            blue_pixels.append(image[i, j])
        if is_flag.is_flag(r, g, b) == "red":
            red_pixels.append(image[i, j])
        if is_flag.is_flag(r, g, b) == "white":
            white_pixels.append(image[i, j])
        if is_flag.is_flag(r, g, b) == "other":
            other_pixels.append(image[i, j])



total_pixels = height*width - len(other_pixels)

red_pixel_percent = len(red_pixels)/total_pixels * 100
blue_pixel_percent = len(blue_pixels)/total_pixels * 100
white_pixel_percent = len(white_pixels)/total_pixels * 100

print(red_pixel_percent)
print(blue_pixel_percent)
print(white_pixel_percent)

if 30 < white_pixel_percent < 40:
    if 30 < red_pixel_percent < 40:
        if 15 < blue_pixel_percent < 35:
            print("There is an american flag.")
else:
    print("There is no american flag.")
