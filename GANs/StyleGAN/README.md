# Stylegan
This is my customized version of the Official Nvidia TensorFlow implementation of the StyleGAN network. The original repository can be found at https://github.com/NVlabs/stylegan.

I have deleted some files that I didn't use, mainly the ProGAN network, metrics I didn't use, and files for interacting with the pre-trained generators.

## Modifications
I made a few minor changes to the network and helper functions.
These were recommended from Gwern's StyleGAN tutorial https://www.gwern.net/Faces.

1. Firstly, I added a print function to the dataset tool, to aid in debugging issues with images. Thankfully, I prepared my datasets correctly and so didn't need to use this.

  I added the below code on line 522 of `dataset_tool.py`

  `# Added the below line on reccomendation from Gwern
    print(image_filenames[order[idx]])`

2. I additionally added a patch based on one presented by Gwern (attributed to 'nsheppard', though without a link). This patch allowed the network to run from the latest snapshot, instead of having to specify the snapshot.

  I added the below code starting on line 122 of `training/misc.py`

    `def locate_latest_pkl():
        allpickles = sorted(glob.glob(os.path.join(config.result_dir, '0*', 'network-*.pkl')))
        latest_pickle = allpickles[-1]
        resume_run_id = os.path.basename(os.path.dirname(latest_pickle))
        RE_KIMG = re.compile('network-snapshot-(\d+).pkl')
        kimg = int(RE_KIMG.match(os.path.basename(latest_pickle)).group(1))
        return (locate_network_pkl(resume_run_id), float(kimg))`

  And I added the below code starting on line 159 of `training/training_loop.py`

    `if resume_run_id == 'latest':
        try:
            network_pkl, resume_kimg = misc.locate_latest_pkl()
            print('Loading networks from "%s"...' % network_pkl)
            G, D, Gs = misc.load_pkl(network_pkl)
        except:
            print('Constructing networks...')
            G = tflib.Network('G', num_channels=training_set.shape[0], resolution=training_set.shape[1], label_size=training_set.label_size, **G_args)
            D = tflib.Network('D', num_channels=training_set.shape[0], resolution=training_set.shape[1], label_size=training_set.label_size, **D_args)
            Gs = G.clone('Gs')`

3. Finally, I commented out a line in the training loop that ran the FID metric at each iteration, to save training time (and only ran it on the snapshots that I chose after training was done)

  I commented out this code on line 285 of `training/training_loop.py`

    `#metrics.run(pkl, run_dir=submit_config.run_dir, num_gpus=submit_config.num_gpus, tf_config=tf_config)`

## Main Parameters
