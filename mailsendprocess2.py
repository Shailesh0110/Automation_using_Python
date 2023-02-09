import mailsendprocess1
from sys import  *
import time

def main():
    print("Process Monitoring Automation with periodic Mail Sender....")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : [AbsolutePath_of_Directory] which you want to delete files")
        exit()

    try:
        mailsendprocess1.main(argv[1])


    except ValueError:
            print("Error : Invalid datatype of input")

    except Exception as E:
            print("Error : Invalid input", E)

if __name__=="__main__":
    main()