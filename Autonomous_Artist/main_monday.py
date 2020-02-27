import argparse
import subprocess


# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("--week", type=str, help="The number of the week")

def main(week):
    # 1: Generate new images
    commands = ['python3', 'generate_images_monday.py','--week',str(week)]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)

    if process.returncode == 0:
        # 2: Add new images to DB
        commands = ['python3', 'add_new_imgs_to_DB_monday.py','--week',str(week)]
        process = subprocess.run(commands,
                                stdout=subprocess.PIPE,
                                universal_newlines=True)

        if process.returncode == 0:
            # 3: Tweet new images
            commands = ['python3', 'tweet_new_imgs_monday.py','--week',str(week)]
            process = subprocess.run(commands,
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)
            #process
        else:
            print ("fail 2")
            print (process)
    else:
        print ("fail 1")
        print (process)

    # 4: Take inventory of ETH and make appropriate sales if needed
    # possibly split this into two functions and do the logic in python ?
    # 2: Add new images to DB
    commands = ['node', 'AA_smart_contract_rinkeby/scripts/send_eth.js']
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)


if __name__ == '__main__':
    args = parser.parse_args()
    week = args.week
    main(week)
