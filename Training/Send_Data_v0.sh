# This script was used to transfer data from my local machine to a remote server
# I did this by uploading the data to github, then cloning and extracting the
# data on the server side.

# It was not run as a full script, but instead the individual lines were
# run in the terminal

# I used this for the beggining of training, before switching to using the
# forklift GUI

########################

# Clone into the repo
$ git clone https://github.com/isaacschaal/stylegan

$ cd stylegan/Data

# Unzip the data
$ unzip  house256-1.zip;  unzip house256-2.zip;  unzip house256-3.zip; unzip  house256-4.zip; unzip  house256-5.zip; unzip trees256-1.zip; unzip trees256-2.zip;

# Make the  directories for the combined data
$ mkdir house256; mkdir trees256

# Move the unzipped folders to thier correct directories
$ mv house256-1 house256; mv house256-2 house256; mv house256-3 house256; mv house256-4 house256; mv house256-5 house256;

$ mv trees256-1 trees256; mv trees256-2 trees256;

# Enter the directory, put all files in subfolders in the main folder
# and then delete the empty  directories (for both datasets)
$ cd trees256; find . -type f -print0 | xargs -0 -I file mv --backup=numbered file . ; rm -r trees256-1; rm -r  trees256-2; cd ..

$ cd house256; find . -type f -print0 | xargs -0 -I file mv --backup=numbered file . ; rm -r house256-1; rm -r  house256-2; rm -r house256-3; rm -r  house256-4; rm -r house256-5; cd ..
