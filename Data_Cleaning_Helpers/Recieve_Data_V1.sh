# This script is used to get data back from the server

# I first removed the Data folder from the src folder, as it was unnecessary 
# and large
$ rm -r results/00000-sgan-trees256-1gpu/src/Data

# And (on my local machine) sent the data to my Downloads folder
$ scp -i path/to/key -r ec2-user@ec2-18-209-238-75.compute-1.amazonaws.com:/home/ec2-user/stylegan/results/00000-sgan-trees256-1gpu/ ~/Downloads
