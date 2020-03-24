# This script was used to get data from the server to my local machine

# It was not run as a full script, but instead the individual lines were
# run in the terminal

# I used this for the beggining of training, before switching to using the
# forklift GUI

########################

# I first removed the Data folder from the src folder, as it was unnecessary
# and large  (this line was run on the remote server)
$ rm -r results/00000-sgan-trees256-1gpu/src/Data

# And sent the data to my Downloads folder (this line was run on my local machine)
$ scp -i path/to/key -r ec2-user@ec2-XX-XXX-XXX-XX.compute-1.amazonaws.com:/home/ec2-user/stylegan/results/00000-sgan-trees256-1gpu/ ~/Downloads
