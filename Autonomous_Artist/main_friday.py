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
    #process

    # 2: Create auction

    # 3: Tweet auction
    commands = ['python3', 'tweet_auction_friday.py','--week',str(week)]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    #process

if __name__ == '__main__':
    args = parser.parse_args()
    week = args.week
    main(week)
