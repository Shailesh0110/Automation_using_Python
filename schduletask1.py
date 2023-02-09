import schedule
import time
import datetime

def Fun():
    print("inside fun",datetime.datetime.now())

def main():
    print("hello",datetime.datetime.now())
    schedule.every(1).minutes.do(Fun)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()