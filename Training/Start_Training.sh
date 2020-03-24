# This script is used for training the StyleGAN network.
# It includes shell commands for converting data
# into tf-records, starting a tmux session,
# training the model, and activating Tensorboard

# It was not run as a full script, but instead the individual lines were
# run in the terminal

########################

# If this was the first time training on a dataset
# the following two lines were run to convert the
# data to TF_records. If they were already created,
# these lines were skipped

# Activate the tensorflow environment
$ source activate tensorflow_p36

# Use the dataset_tool to convert the jpg images into tf-records, which
# must be used for the model
$ python dataset_tool.py create_from_images datasets/garden512 Data/garden512/

# Skip to here if tf-records were already created

# Start a tmux session
$ tmux new -s main_training

# Activate the environment
# Note: I found the below code the only way for
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
$ tensorboard --logdir results/00000-sgan-garden512-1gpu/

# And connected to it on my local machine with this
# (the ip adress of the server must be changed ) (This was run on my local machine)
$ ssh -i path/to/key -NL 6006:localhost:6006 ec2-user@ec2-XX-XXX-XXX-XX.compute-1.amazonaws.com
