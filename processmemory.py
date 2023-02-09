import os
from sys import  *
import psutil
import time

def Display(log_dir = "Shailesh"):

    listprocess=[]

    if (os.path.exists(log_dir)):
        print("already exist")
    else:
        fd = open(log_dir, "w")

    separator="_"*80
    log_path=os.path.join(log_dir,"Shailesh%s.log"%(time.ctime()))

    fd=open(log_dir,"w")
    fd = open(log_dir, "a")

    fd.write(separator+"\n")
    fd.write("Shailesh systeem process logeer"+time.ctime()+"\n")
    fd.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            printinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            printinfo['Memory(MB)'] = vms
            listprocess.append(printinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for i in listprocess:
        fd.write("%s\n"% i)

def main():
    print("********Shailesh systeem***********")
    print("Application name :"+argv[0])


    if (len(argv) != 2):
        print("Error:invalid number of arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if (argv[1]=="-h") or (argv[1]=="-H"):
        print("this script is used for record of running process")
        exit()

    if (argv[1]=="-u") or (argv[1]=="-U"):
        print("usage:Application name Absolutepath of_directory")
        exit()

    ret=Display(argv[1])
    print(ret)
    '''try:
        Display(argv[1])

    except ValueError:
        print("Error:invalid datatype of input")
    except Exception:
        print("Error:invalide input")'''

if __name__=="__main__":
    main()
