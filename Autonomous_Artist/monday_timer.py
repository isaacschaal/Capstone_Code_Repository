import schedule
import time
import subprocess

def job():
    commands = ['nohup','python3', 'time_test.py']
    process = subprocess.run(commands,
                            stdout=subprocess.PIPE,
                            universal_newlines=True)
    print (process.stdout)


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(10) # wait one minute
