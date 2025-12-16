FUNCTION AND DETECTION:
My program will detect if an image has a russian, french or american flag on it. If around 25-50% of the image is red, and 25-50% of the flag is white, and around 10-30% of the image is blue then my program will determine that there is one of those flags in it. My program will add 1 to a counter for every correctly colored pixel and subtract one for an irrelevant pixel, then divide that by the total pixels to find the rough percentage that there is a russian french or amercian flag. It will go through every image and display the percentage or red, blue and white colors in the image, along with the image number and the percentage of relevant pixels(% chance of a flag being present.)

TESTING, ROBUSTNESS AND CHALLENGES:
I tested the selection sort algorithm by printing the sorted list after, which was from smallest to biggest. This wouldn't work, since my binary search relied on the selection search to first sort the list but the binary search needed the list biggest to smallest. All i did to fix this issue was switch the < symbol to the > symbol, which sent the highest number in the list to the start instead of the other way around. Another test and big issue i faced was not being able to take the width and height from every specific image, since the program need the unloaded image to take the height and witdh but the unloaded image to run the program. I printed the width for every image and realized they were all different, and so i made a for loop that appended the unloaded image to a list first, then loaded the image. Then i had two lists for both scenarios.

PERFORMANCE ANALYSIS AND PROFILING:
I profiled the start to the end of the entire code, and it takes around 3-4 seconds for it to run. The binary search takes around 1-2 seconds, and the selection sort takes around 1 second. Keep in mind that the pause while the user inputs a percentage is not included in any of the times.



Choose a specific theme for which you will be scanning multiple images (3 pts)
- [ ] Clearly define the visual feature your program will detect and count (2 pts)
- [ ] Justify your feature detection with an explanation of how your chosen feature can be accurately identified (3 pts)
Testing and robustness: include a section in your README describing testing done to ensure each of the tasks works as intended (1 pt)
- [ ] Performance analysis: include a section in your README describing your code profiling: give an example of the report and discuss what parts of the program take the longest
- [ ] Challenges faced: include a section in your README describing at least one challenge faced and how you overcame it (2 pts)
