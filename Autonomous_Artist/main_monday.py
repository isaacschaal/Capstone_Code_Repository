import argparse
import subprocess


# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("--week", type=str, help="The number of the week")

def main(week):
    # On sunday should make the images? So they are ready? Or monday morning?
    # TO DO, generate images and add to folder

    # 1: Add new images to DB
    commands = ['python3', 'add_new_imgs_to_DB_monday.py','--week',str(week)]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
                            
    if process.returncode == 0:

        # 2: Tweet new images
        commands = ['python3', 'tweet_new_imgs_monday.py','--week',str(week)]
        process = subprocess.run(commands,
                                stdout=subprocess.PIPE,
                                universal_newlines=True)
        #process


if __name__ == '__main__':
    args = parser.parse_args()
    week = args.week
    main(week)
