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
Funnily enough, if you look at my folder where I worked on this, I have 20 pictures, which included the answer, the input, and 18 different ideas I tried. I started off just trying to use edge detection for a few of those iterations but I wasn't sure how to zero in on the shape and was a little too stubborn to look it up. I then turned to color detection. The funny thing is, one of my earlier iterations of color detection gave me a very decent object detection device but I threw it out right away and started focusing more on the points because I kept trying to visualize it as a graph where each object was a point. I spent way too long trying to mess with it but I just couldn't get it to ignore the red door on the left. When I took a short break, I realized I already had the object detection thing so I threw out a couple hours of work and built off one of my earliest rejected ideas. I had the filter ignore boxes that are either too large or too small (took a little bit of brute forcing here) and I finally had it pretty close but for some reason, the algorithm I was using just refused to fit the line correctly (because of a couple of outliers. After a little while of trying to mess with it, I realized I could just use machine learning so I imported scikitlearn and used RANSAC to fit the lines and it immediately snapped into place.

## Libraries
I used three libraries: cv2, numpy, and scikitlearn
