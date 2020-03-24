# This script is used to take picture with
# the laptop's built in webcam

########################

import numpy as np
import cv2
import time
import os
import re

# Find the id of the last picture taken (highest id)
# and start +1 from there
file_list = os.listdir(path='./selfies')
num_list = [re.findall(r'\d+', string) for string in file_list]
one_list = [int(num[0]) for num in num_list if len(num) >0]
max_dig = max(one_list)
new_start = max_dig + 1

# Sleep to give me time to switch desktops to
# an empty with just the background image
time.sleep(3)

# Start the feed from the camera
cap = cv2.VideoCapture(0)

# Take ten pictures, which is aligned
# with my miror routine to take ten
# pictures at different angles
for i in range(10):
    # pause so that I can adjust the angle
    time.sleep(2)

    # get a still from the camera
    _, frame = cap.read()

    print (".")
    # play audio to know when to switch the angle
    os.system( "say p" )
    # save the photo
    cv2.imwrite('selfies/frame-'+str(new_start+i)+'.png',frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

print ("Done")
