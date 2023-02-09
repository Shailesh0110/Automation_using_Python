from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buffer=fd.read(blocksize)
    while len(buffer)>0:
        hasher.update(buffer)
        buffer=fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()


def Displaychecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            print("Current folder is : " + foldername)
            for filen in filname:
                path=os.path.join(foldername,filen)
                file_hash=hashfile(path)
                print(path)
                print(file_hash)
                print(" ")
    else:
        print("Invalid Path")


def main():
    print("---- Marvellous Infosystems by Piyush Khairnar-----")

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
       Displaychecksum(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)


if __name__ == "__main__":
    main()