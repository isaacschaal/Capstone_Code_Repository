import argparse
import subprocess
from create_db import Artwork, Session



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

        if process.returncode == 0:
            # 3: Create auction
            # Get the tokenid and favorite count
            session = Session()
            tokenID, favorites  = session.query(Artwork.tokenID, Artwork.favorites).filter_by(week = week, winner = True).first()
            session.close()

            # run the node auction script
            commands = ['node', 'AA_smart_contract_rinkeby/scripts/sell.js',
                        '-f',str(favorites),
                        '-i',str(tokenID)]
            process = subprocess.run(commands,
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)

            if process.returncode == 0:
                # 4: Tweet auction
                stdout = process.stdout

                # get the auction link
                auction_link = stdout.split("order!",1)[1].strip()

                # save it to the DB
                session = Session()
                u  = session.query(Artwork).filter_by(week = week, winner = True).first()
                u.auction_link =  auction_link
                session.commit()
                session.close()

                commands = ['python3', 'tweet_auction_friday.py','--week',str(week)]
                process = subprocess.run(commands,
                                        stdout=subprocess.PIPE,
                                        universal_newlines=True)
                #process



    else:
        print (process)



if __name__ == '__main__':
    args = parser.parse_args()
    week = args.week
    main(week)
