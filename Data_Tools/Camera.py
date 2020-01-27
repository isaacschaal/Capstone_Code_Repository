import numpy as np
import cv2
import time
import os
import re

file_list = os.listdir(path='./selfies')
num_list = [re.findall(r'\d+', string) for string in file_list]
max_dig = max(num_list)
new_start = int(max_dig[0]) + 1

# give me time to switch desktops to
# an empty with just the background image
time.sleep(5)

#start the feed from the camera
cap = cv2.VideoCapture(0)

# take ten pictures, which is aligned
# with my miror routine to take 10
# pictures at different angles
for i in range(10):
    # pause so that I can adjust the angle
    time.sleep(3)

    # get a still from the camera
    _, frame = cap.read()

    print (".")
    # play audio to know when to switch
    # the angle
    os.system( "say p" )
    # save the photo
    cv2.imwrite('selfies/frame-'+str(new_start+i)+'.png',frame)



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

print ("Done :)")
