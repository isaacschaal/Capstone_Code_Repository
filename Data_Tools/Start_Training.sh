# This script is used to start training
# TO DO: Change the results folder and ip address to be
#        generic

# I start a session
$ tmux new -s main_training

# I found the below code the only way for 
# the environment to set up properly
# and have access to TF
$ source activate tensorflow_p36
$ conda deactivate
$ conda activate tensorflow_p36

# I used the following code to make the model restart training if it crashes.
# I had to use the “resume from last pkl” patch in order to use this.
$ while true; do python train.py ; date; sleep 10s; done

# I started a new window in the session and used this to 
# start Tensorboard
$ tensorboard --logdir results/00000-sgan-trees256-1gpu/

# And connected to it on my local machine with this
# (the ip adress of the server must be changed )
$ ssh -i path/to/key -NL 6006:localhost:6006 ec2-user@ec2-18-209-238-75.compute-1.amazonaws.com
