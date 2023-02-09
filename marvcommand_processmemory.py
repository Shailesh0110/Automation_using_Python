import os
from sys import  *
import psutil
import time,datetime
import schedule

def Display(log_dir="Shailesh"):
    listprocess=[]
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="_"*80
    log_path=os.path.join(log_dir,"Shailesh%s.log"%(time.time()))
    f=open(log_path,'w')

    f.write(separator+"\n")
    f.write("Shailesh systeem process logeer above 50MB :"+(time.ctime())+"\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            printinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

            vms = int(proc.memory_info().vms / (1024 * 1024))
            if vms>50:
                printinfo['Memory(MB)'] = vms
                listprocess.append(printinfo)
            else:
                pass
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    for i in listprocess:
        f.write("%s\n"% i)
    f.write("Number of process recorded:%s\n" % len(listprocess))


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

    try:
        print("start log file scanning", datetime.datetime.now())
        schedule.every(int(argv[1])).minutes.do(Display)

        #Display(argv[1])
        while (True):
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error:invalid datatype of input")
    except Exception as E:
        print("Error:invalide input",E)

if __name__=="__main__":
    main()
