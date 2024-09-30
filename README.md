## Wisconsin Autonomous Perception Coding Challenge

 ![](https://github.com/mp0549/WAPCC/blob/main/finalanswer.png)

 ## Methodology
 1. Load the image in and convert it to HSV to detect colors better
 2. Two masks are created to isolate the red cones using specified HSV color ranges. These masks are combined to create a single mask representing the red areas.
 3. Erode and Dilate to improve the contour. Then identify contours in the mask to identify the boundaries
 4. Filter the contours based on area and perimeter to disregard very large and small objects- also helps avoid random splashes of red that may have been in the picture as a result of the lighting
 5. Separate the boxes into left and right to be able to make one line on each side
 6. Line fitting using scikitlearn RANSAC and drawing it on the picture while avoiding outliers
 7. Save it as finalanswer.png

## The Story
Funnily enough, if you peek into my project folder, you’ll find 20 pictures in there: the input image, the final answer, and a whopping 18 different versions where I was experimenting with ideas. At first, I went all in on edge detection, trying to make it work, but I couldn’t quite figure out how to zero in on the shape, and honestly, I was a little too stubborn to look up how to do it.
So, I decided to switch gears to color detection. Ironically, one of my earliest attempts at color detection actually gave me a decent object detection system. But I tossed that aside because, for some reason, I was obsessed with treating it like a graph where each cone was a point. Naturally, I spent way too long trying to force this approach to work, but no matter how I messed with it, I couldn’t stop the algorithm from getting confused by the red door on the left.
After taking a short break and clearing my head, I realized I already had a working object detection setup. So, I basically threw out a couple of hours of work and decided to go back to my original idea. I added a filter to ignore boxes that were too large or too small. But then the line-fitting algorithm kept messing up because of some annoying boxes in the back. After trying to mess with the line fitting a bit, I turned to machine learning and used RANSAC to fit the lines.






## Libraries
I used three libraries: cv2, numpy, and scikitlearn
