# This was my first cropping script. It crops a set of
# 720x1080 images into 3 images (left, middle, right) of size 720x720
# and into 5 random images of size 600x600 in random places (not too close
# to the eges). It was used in early iterations but not in any final datasets.

########################

from PIL import Image
import glob
import os
import random

# Start the naming
j = 0
for fn in glob.glob('photos/*.jpg'):
    # Create an array to store the crops
    new_ims = []
    # Open the image
    im = Image.open(fn)
    # Crop right, center, and left
    new_ims.append( im.crop((0, 0, 720, 720)) )
    new_ims.append(im.crop((180, 0, 900, 720)) )
    new_ims.append(im.crop((360, 0, 1080, 720)) )
    # Make 5 random crops
    for i in range(5):
        xoff = random.randint(20,460)
        yoff = random.randint(20,100)
        new_ims.append( im.crop((0+xoff, 0+yoff, 1080-(480-xoff), 720-(120-yoff))) )
    # Save the images
    for new_im in new_ims:
        new_im = new_im.save(str(j) + "cropped.jpg")
        j+=1
