FUNCTION AND DETECTION:
My program will detect if an image has a russian, french or american flag on it. If around 25-50% of the image is red, and 25-50% of the flag is white, and around 10-30% of the image is blue then my program will determine that there is one of those flags in it. My program will add 1 to a counter for every correctly colored pixel and subtract one for an irrelevant pixel, then divide that by the total pixels to find the rough percentage that there is a russian french or amercian flag. It will go through every image and display the percentage or red, blue and white colors in the image, along with the image number and the percentage of relevant pixels(% chance of a flag being present.)

TESTING, ROBUSTNESS AND CHALLENGES:
I tested the selection sort algorithm by printing the sorted list after, which was from smallest to biggest. This wouldn't work, since my binary search relied on the selection search to first sort the list but the binary search needed the list biggest to smallest. All i did to fix this issue was switch the < symbol to the > symbol, which sent the highest number in the list to the start instead of the other way around. Another test and big issue i faced was not being able to take the width and height from every specific image, since the program need the unloaded image to take the height and witdh but the unloaded image to run the program. I printed the width for every image and realized they were all different, and so i made a for loop that appended the unloaded image to a list first, then loaded the image. Then i had two lists for both scenarios. The hardest challenge i faced was my binary search was using the partially-sorted list that was only going down, and it needed to be ascending. So i made a second selection sort, one for displaying the top five percentages, and one for the binary search.

PERFORMANCE ANALYSIS AND PROFILING:
I profiled the start to the end of the entire code, and it takes around 3-4 seconds for it to run. The binary search takes around 1-2 seconds, and the selection sort takes around 1 second. Keep in mind that the pause while the user inputs a percentage is not included in any of the times.



