import argparse
import subprocess


# Parse Args
parser = argparse.ArgumentParser()
parser.add_argument("--week", type=str, help="The number of the week")

def main(week):
    # 1: Choose Winner
    commands = ['python3', 'tw_choose_winner_friday.py','--week',str(week)]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    if process.returncode == 0:

        # 2: Mint token and add metadata
        commands = ['python3', 'mint_friday.py','--week',str(week)]
        process = subprocess.run(commands,
                                stdout=subprocess.PIPE,
                                universal_newlines=True)
        #process

        # 3: Create auction

        # 4: Tweet auction
        # commands = ['python3', 'tweet_auction_friday.py','--week',str(week)]
        # process = subprocess.run(commands,
        #                         stdout=subprocess.PIPE,
        #                         universal_newlines=True)
        # #process
    else:
        print (process)



if __name__ == '__main__':
    args = parser.parse_args()
    week = args.week
    main(week)
