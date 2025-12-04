from PIL import Image
import is_flag
import math
import time

images = []
images2 = []

start = time.time()
image = Image.open("6.7/americanflag1.jpg").load()
image_output = Image.open("6.7/americanflag1.jpg")
images.append(image)
images2.append(image_output)

image2 = Image.open("6.7/americanflag2.webp").load()
image2_output = Image.open("6.7/americanflag2.webp")
images.append(image2)
images2.append(image2_output)

image3 = Image.open("6.7/americanflag3.webp").load()
image3_output = Image.open("6.7/americanflag3.webp")
images.append(image3)
images2.append(image3_output)

image4 = Image.open("6.7/americanflag4.jpg").load()
image4_output = Image.open("6.7/americanflag4.jpg")
images.append(image4)
images2.append(image4_output)

image5 = Image.open("6.7/americanflag5.jpg").load()
image5_output = Image.open("6.7/americanflag5.jpg")
images.append(image5)
images2.append(image5_output)

image6 = Image.open("6.7/americanflag6.jpg").load()
image6_output = Image.open("6.7/americanflag6.jpg")
images.append(image6)
images2.append(image6_output)





blue_pixels = []
red_pixels = []
white_pixels = []
other_pixels = []
for x in range(len(images2)):
    width = images2[x].width
    height = images2[x].height
    for a in range(len(images)):
        for i in range(width):
            for j in range(height):
                r = images[a][i,j][0]
                g = images[a][i,j][1]
                b = images[a][i,j][2]

                if is_flag.is_flag(r, g, b) == "blue":
                    blue_pixels.append(images[a][i, j])
                if is_flag.is_flag(r, g, b) == "red":
                    red_pixels.append(images[a][i, j])
                if is_flag.is_flag(r, g, b) == "white":
                    white_pixels.append(images[a][i, j])
                if is_flag.is_flag(r, g, b) == "other":
                    other_pixels.append(images[a][i, j])

                total_pixels = height*width - len(other_pixels)

                red_pixel_percent = math.ceil(len(red_pixels)/total_pixels * 100)
                blue_pixel_percent = math.ceil(len(blue_pixels)/total_pixels * 100)
                white_pixel_percent = math.ceil(len(white_pixels)/total_pixels * 100)

        print(red_pixel_percent)
        print(blue_pixel_percent)
        print(white_pixel_percent)

        blue_pixels = []
        red_pixels = []
        white_pixels = []
        other_pixels = []

        if 50 <= white_pixel_percent <= 70:
            if 25 <= red_pixel_percent <= 60:
                if 10 <= blue_pixel_percent <= 30:
                    print("There is an american flag.")
        else:
            print("There is no american flag.")





end = time.time()
total_time = end - start

print("It took {:.3f} seconds for the code to run".format(total_time))
