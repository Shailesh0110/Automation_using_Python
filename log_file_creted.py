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
                vms = proc.memory_info().vms / (1024 * 1024)
                printinfo['Memory(MB)'] = vms
                listprocess.append(printinfo)

            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        for i in listprocess:
            fd.write("%s\n" % i)
        fd.write("______________________Endfile______________________")



        print("******File log is created********")


def main():
    print("marvellous family")
    print("application name:"+argv[0])

    if (len(argv) < 2):
        print("Error:invalid number of arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("this script is used for record of running process")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage:Application name Absolutepath of_directory")
        exit()

    try:
        write_file(argv[1])

    except ValueError:
        print("Error:invalid datatype of input")
    except Exception:
        print("Error:invalide input")



if __name__=="__main__":
    main()