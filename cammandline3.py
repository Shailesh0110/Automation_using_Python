from sys import *
import getopt
import argparse

def fun(parameter):
    print("hello")

def main():
    print("marvellous family")
    print("application name:"+argv[0])

    if (len(argv))!=3:
        print("error:invalid argument")
        exit()
    if argv[1]=="-h":
        print("this script is designed for_______")
        exit()

    if argv[1]=="-u":
        print("usage:application name_______")
        exit()

    try:
        fun(argv[1])
    except Exception as E:
        print("Error:invalid input"+E)

    if ((len(argv)<1) or (len(argv)>3)):
        print("invalid number of arguments")


if __name__=="__main__":
    main()