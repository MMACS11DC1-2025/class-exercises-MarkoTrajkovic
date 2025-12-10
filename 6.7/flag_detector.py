from PIL import Image
import is_flag
import math
import time

images = []
images_raw = []
probability = []

start = time.time()

# Load all images
images2 = ["6.7/americanflag1.jpg",
    "6.7/americanflag2.webp",
    "6.7/americanflag3.webp",
    "6.7/americanflag4.jpg",
    "6.7/americanflag5.jpg",
    "6.7/americanflag6.jpg",
    "6.7/serbianflag.webp"]

for a in images2:
    img_raw = Image.open(a)
    images_raw.append(img_raw)
    images.append(img_raw.load())


for x in range(len(images_raw)):
    count = 0
    counter = 0
    img_raw = images_raw[x]   # actual image object
    img = images[x]

    width, height = img_raw.width, img_raw.height

    blue_pixels = []
    red_pixels = []
    white_pixels = []
    other_pixels = []

    for i in range(width):
        for j in range(height):

            r, g, b = img[i, j]

            color = is_flag.is_flag(r, g, b)

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

    total_pixels = width * height

    if total_pixels == 0:
        print("Image", x+1, ": Cannot calculate (no valid pixels)")
        continue

    red_percent = math.ceil(len(red_pixels) / total_pixels * 100)
    blue_percent = math.ceil(len(blue_pixels) / total_pixels * 100)
    white_percent = math.ceil(len(white_pixels) / total_pixels * 100)

    print("Image", x+1)
    print("Red:", red_percent)
    print("Blue:", blue_percent)
    print("White:", white_percent)



    pixel_percent = (counter/total_pixels)*100
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

def search(probabilities):
    for i in range(len(probabilities)):
        smallest_score = probabilities[i]
        smallest_index = i

        for j in range(i+1, len(probabilities)):
            if probabilities[j] < smallest_score:
                smallest_score = probabilities[j]
                smallest_index = j
        probabilities[smallest_index], probabilities[i] = probabilities[i], probabilities[smallest_index]
        top_five = probabilities[-5:]
        print(top_five)

sorted_list = search(probability)

def binary(list, query):
    start = 0
    end = len(list)-1

    while start <= end:
        middle = int((start+end)/2)
        if list[middle][0] == query:
            print(query + 1)
        elif list[middle][0] > query:
            end = middle-1
        else:
            start = middle + 1
    return -1
binary(sorted_list, 94.14)



    

end = time.time()
print("It took {:.3f} seconds to run".format(end - start))
