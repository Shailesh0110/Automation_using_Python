import os
from sys import  *
import psutil
import time

def Display_procss():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            printinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            printinfo['Memory(MB)'] = vms
            listprocess.append(printinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for i in listprocess:
        print(i)

def main():
    print("*********marvellous infosysteem:python Automation************")

    print("Process Monitor with memory usage")

    Display_procss()


if __name__=="__main__":
    main()