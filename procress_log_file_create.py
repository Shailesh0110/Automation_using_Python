import os
from sys import  *
import psutil
import time

def write_file(filename):

    if(os.path.exists(filename)):
        print("File alredy exist create new file")
    else:
        fd = open(filename, "w")
        fd = open(filename, "a")

        data = "_" * 80
        fd.write(data + "\n")
        fd.write("Shailesh systeem process logeer" + time.ctime() + "\n")
        fd.write(data + "\n")

        fd = open(filename, "a")

        listprocess = []

        for proc in psutil.process_iter():
            try:
                printinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                printinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
                listprocess.append(printinfo)

            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        for i in listprocess:
            fd.write("%s\n" % i)
        fd.write("______________________Endfile______________________")



        print("******File log is created********")


def main():
    print("Enter the file name create")
    name= input()

    write_file(name)

if __name__=="__main__":
    main()