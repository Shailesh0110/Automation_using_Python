import schedule
import time
import datetime

def task_minute():
    print("inside task minute:",datetime.datetime.now())

def task_hour():
    print("inside task hour:",datetime.datetime.now())

def task_day():
    print("inside task day:",datetime.datetime.now())


def main():
    print("inside main function:",datetime.datetime.now())

    schedule.every(1).minutes.do(task_minute)
    schedule.every(1).hour.do(task_hour)
    schedule.every().wednesday.at('14:00').do(task_day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()