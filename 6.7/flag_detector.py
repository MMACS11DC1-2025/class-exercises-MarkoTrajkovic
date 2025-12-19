from PIL import Image
import is_flag
import math
import time

#defines the lists
images = []
images_raw = []
probability = []
paired_data = []

start = time.time()

#List of images used
images2 = [
    "6.7/americanflag1.jpg",
    "6.7/americanflag2.webp",
    "6.7/americanflag3.webp",
    "6.7/americanflag4.jpg",
    "6.7/americanflag5.jpg",
    "6.7/americanflag6.jpg",
    "6.7/serbianflag.webp",
    "6.7/americanflag7.jpg",
    "6.7/frenchflag.png",
    "6.7/russianflag.webp"
]

#Seperates loaded and unloaded lists by appending the unloaded list, then loading the list outside.
for a in images2:
    img_raw = Image.open(a)
    images_raw.append(img_raw)
    images.append(img_raw.load())

#goes through all the images and takes the width and height from each one.
for x in range(len(images_raw)):
    counter = 0
    img_raw = images_raw[x]
    img = images[x]

    width, height = img_raw.width, img_raw.height

    #more lists being initialized
    blue_pixels = []
    red_pixels = []
    white_pixels = []
    other_pixels = []

    #uses nested lists to go through every pixel and uses the is_flag program to assign a clolor to each.
    for i in range(width):
        for j in range(height):
            r, g, b = img[i, j]
            color = is_flag.is_flag(r, g, b)

            #assigned each pixel to their color lists
            if color == "blue":
                blue_pixels.append((r, g, b))
                counter += 1
            elif color == "red":
                red_pixels.append((r, g, b))
                counter += 1
            elif color == "white":
                white_pixels.append((r, g, b))
                counter += 1
            else:
                other_pixels.append((r, g, b))
                counter -= 1

    #error control, 
    total_pixels = width * height
    if total_pixels == 0:
        continue
    
    #makes the percentages for each color of the image.
    red_percent = math.ceil(len(red_pixels) / total_pixels * 100)
    blue_percent = math.ceil(len(blue_pixels) / total_pixels * 100)
    white_percent = math.ceil(len(white_pixels) / total_pixels * 100)

    print("Image", x + 1)
    print("Red:", red_percent)
    print("Blue:", blue_percent)
    print("White:", white_percent)

    pixel_percent = (counter / total_pixels) * 100
    paired_data.append((pixel_percent, images2[x]))
    probability.append(pixel_percent)

    print(pixel_percent)
    if pixel_percent >= 90:
        print("This is most likely an american, russian or french flag.")
    elif pixel_percent >= 60:
        print("There might be an american, russian or french flag.")
    elif pixel_percent >= 30:
        print("It is unlikely there is an american, russian or french flag.")
    else:
        print("There is no american, russian or french flag.")

# ---------------- SELECTION SORT (ASCENDING) ----------------
def selection_sort_ascending(data):
    data = data[:]  # copy list
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j][0] < data[min_index][0]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data

# ---------------- SELECTION SORT (DESCENDING) ----------------
def selection_sort_descending(data):
    data = data[:]
    for i in range(len(data)):
        max_index = i
        for j in range(i + 1, len(data)):
            if data[j][0] > data[max_index][0]:
                max_index = j
        data[i], data[max_index] = data[max_index], data[i]
    return data

# sort for binary search (ascending)
paired_data_sorted = selection_sort_ascending(paired_data)

# sort for top 5 (descending)
top_5 = selection_sort_descending(paired_data)[:5]

print("Top 5 most likely percentages:")
for item in top_5:
    print(item)

# ---------------- BINARY SEARCH ----------------
def binary(data, query):
    start = 0
    end = len(data) - 1

    target_min = query - 0.5
    target_max = query + 0.5

    while start <= end:
        middle = (start + end) // 2
        score, img = data[middle]

        if target_min <= score <= target_max:
            return score, img
        elif score > query:
            end = middle - 1
        else:
            start = middle + 1

    return "Sorry, there is no image with a percentage like that."

pause_start = time.time()
answer = float(input("Type one of the top percentages: "))
pause_end = time.time()

print(binary(paired_data_sorted, answer))

end = time.time()
print("It took {:.3f} seconds to run".format(end - start - (pause_end - pause_start)))
