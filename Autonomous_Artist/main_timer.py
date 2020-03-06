import schedule
import time
import subprocess

def main_monday():
    commands = ['nohup','python3', 'main_monday.py', '--d', str(datetime.today().strftime('%Y-%m-%d'))]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    print (process.stdout)

def main_friday():
    commands = ['nohup','python3', 'main_friday.py', '--d', str(datetime.today().strftime('%Y-%m-%d'))]
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    print (process.stdout)


schedule.every().day.at("02:45").do(main_monday)
schedule.every().day.at("03:15").do(main_friday)


while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
