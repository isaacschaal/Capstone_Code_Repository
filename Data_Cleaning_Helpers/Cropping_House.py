from PIL import Image 
import glob
import os
import random
 
#Start the naming
j = 0
for fn in glob.glob('photos/*.jpg'):
    #create an array to store the crops
    new_ims = []
    #open the image
    im = Image.open(fn)
    #crop right, center, and left
    new_ims.append( im.crop((0, 0, 720, 720)) )
    new_ims.append(im.crop((180, 0, 900, 720)) )
    new_ims.append(im.crop((360, 0, 1080, 720)) )
    #make 5 random crops
    for i in range(5):
        xoff = random.randint(20,460)
        yoff = random.randint(20,100)
        new_ims.append( im.crop((0+xoff, 0+yoff, 1080-(480-xoff), 720-(120-yoff))) )
    #save the images
    for new_im in new_ims:
        new_im = new_im.save(str(j) + "cropped.jpg") 
        j+=1
