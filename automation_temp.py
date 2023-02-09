from sys import *
from os import *

def Script_task(no):
     if no%2==0:
        print("even")
     else:
        print("odd")

def main():
    print("******************marvellous Automation*************")
    print("Autommation Script Started with name:",argv[0])

    if (len(argv) !=2):
        print("Error:insufficent argument")
        print("use -h for help and use -u for usage")
        exit()


    if (argv[1]=="-h") or (argv[1]=="-H"):
        print("Help:This scipt is used for perform_____________")
        exit()

    elif ((argv[1]=="-u")) or (argv[1]=="-U"):
        print("usage: Provide ____ number of agrumnent as")
        print("first argument is:_____")
        print("second argument is:_____")
        exit()

    else:
        Script_task(int(argv[1]))

if __name__=="__main__":
    main()