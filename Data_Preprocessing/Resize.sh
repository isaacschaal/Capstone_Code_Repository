# This script is used to resize the files before feeding them to StyleGAN
# It is very important that each file is exactly the same, as any deviations
# will cause StyleGAN to crash

# This script is a modified version of a script from Gwern’s StyleGAN Blog post, which can be found at
# https://www.gwern.net/Faces

########################

# Replace "folder" with the actual folder name where the files are stored

find folder/ -type f | xargs -P 16 -n 9000 \
    mogrify -resize 512x512\> -extent 512x512\> -gravity center

# this script preserves the aspect ratio of images by adding white to the edges
# it can also be modified to include black by adding
# a "-background black" tag (the default is white) at the end

# the \> flag means that it will only shrink but not expand images, 
# so images smaller than the desired size will have a background filled in

# To Resize to another dimension besides 512x512, you can simply
# change those numbers to the dimensions required (i.e. 256x256)
