#import everything I will need, math is for ceil function, which rounds up to the nearest whole number
from PIL import Image
import is_flag
import math
import time

#initializing list variables
images = []
images_raw = []
probability = []
paired_data = []

#start a timer for profiling
start = time.time()

#make a list of all images
images2 = ["6.7/americanflag1.jpg",
    "6.7/americanflag2.webp",
    "6.7/americanflag3.webp",
    "6.7/americanflag4.jpg",
    "6.7/americanflag5.jpg",
    "6.7/americanflag6.jpg",
    "6.7/serbianflag.webp",
    "6.7/americanflag7.jpg",
    "6.7/frenchflag.png"]

#loads images and adds unloaded and loaded images to seperate lists
for a in images2:
    img_raw = Image.open(a)
    images_raw.append(img_raw)
    images.append(img_raw.load())

#goes through all the images and notes the width and height of each image
for x in range(len(images_raw)):
    counter = 0
    img_raw = images_raw[x]   
    img = images[x]

    width, height = img_raw.width, img_raw.height

    #initialize more lists
    blue_pixels = []
    red_pixels = []
    white_pixels = []
    other_pixels = []

    #goes through every pixel and appends them to the list of their color
    for i in range(width):
        for j in range(height):

            r, g, b = img[i, j]

            color = is_flag.is_flag(r, g, b)

            #counter goes up by one if there is an american french or russian flag color and down if there is another color. This is used later for finding flag probability.
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

    #takes the width and height from every image. This is to prevent an out of bounds value.
    total_pixels = width * height

    #Error control, if there are no pixels (no image) the program will skip that file.
    if total_pixels == 0:
        print("Image", x+1, ": Cannot calculate (no valid pixels)")
        continue

    #find the approximate percentage of the image that are the correct colors.
    red_percent = math.ceil(len(red_pixels) / total_pixels * 100)
    blue_percent = math.ceil(len(blue_pixels) / total_pixels * 100)
    white_percent = math.ceil(len(white_pixels) / total_pixels * 100)

    #prints every image with the corresponding color percentage.
    print("Image", x+1)
    print("Red:", red_percent)
    print("Blue:", blue_percent)
    print("White:", white_percent)

    #find the percent chance of the flag matching criteria, and appends a list of percentages and a list of percentages plus the image counterpart
    pixel_percent = (counter/total_pixels)*100
    paired_data.append((pixel_percent, images2[x]))
    probability.append(pixel_percent)

    #will respond to each image depending on the probability of a flag.
    print(pixel_percent)
    if pixel_percent >= 90:
        print("This is most likely an american, russian or french flag.")
    elif pixel_percent >= 60:
        print("There might be an american, russian or french flag.")
    elif pixel_percent >= 30:
        print("It is unlikely there is an american, russian or french flag.")
    else:
        print("There is no american, russian or french flag.")

#selection sort algorithm, keeps finding the highest percentage in the list and putting it at the start until the list is highest to lowest.
def search(probabilities):
    for i in range(len(probabilities)):
        highest_score = probabilities[i]
        highest_index = i

        #if the next number is bigger than the previous number, that becomes the new biggest number.
        for j in range(i + 1, len(probabilities)):
            if probabilities[j] > highest_score:
                highest_score = probabilities[j]
                highest_index = j
        
        #replaces the highest number with the place of the highest number.
        probabilities[highest_index], probabilities[i] = probabilities[i], probabilities[highest_index]
    #returns the top 5 highest numbers.
    return probabilities[:5]

#makes a variable for the sorted percentages and the image counterpart, and a variable for just the sorted percentages.
sorted_list = search(paired_data)
sorted_probs = search(probability)

#binary search, will divide the list in half until it finds a percentage that matches with a user input, within a margin of 0.5%
def binary(list, query):
    start = 0
    end = len(list)-1
    #lets the number inputted by the user sway by 0.5
    target_score_min = query - 0.5
    target_score_max = query + 0.5

    while start <= end:
        #cuts the list in half and checks the middle.
        middle = int((start+end)/2)
        score, img = list[middle]
        #if the middle of the list includes the thing the user is seaching for, return that number and picture.
        if target_score_min <= list[middle][0] <= target_score_max:
            return score, img
        #if it is bigger or smaller than what the user put, takes the number under/over that and finds the middle between that number and the other number.
        elif list[middle][0] > query:
            end = middle-1
        else:
            start = middle + 1
    #if there is no match the program will say this.
    return "Sorry, there is no image with a percentage like that."

#prints the top 5 most likely percentages, then asks the user to pick one of them. Then the program uses the binary search to give back the percentage and image of the percentage the user chooses.
#makes a new timer to subtract the pause time between the user input from the total time.
print("The top 5 most likely percentages are:")
print(sorted_probs)
pause_start = time.time()
answer = float(input("Type in a percentage out of these, and I will give you the image. (Please round to the nearest decimal place.) "))
pause_end = time.time()
print(binary(sorted_list, answer))



    
#ends the timer initialized at the start, then prints the time for the entire code to run. Also removes the time the user took to input a number.
end = time.time()
pause = pause_end - pause_start
print("It took {:.3f} seconds to run".format(end - start - pause))
