import  os
from sys import  *

def dict_watcher(dir_name):
    print("inside direct watcher method")
    print("name of input dir:",dir_name)
    print("************Start of Folder ****************")

    for foldername,subfolder,filename in os.walk(dir_name):
        print("folder name is :"+foldername)
        for subf in subfolder:
            print("subfolder name "+foldername+ " is:"+subf)
        for fnames in filename:
            print("file name " + foldername + " is: " + fnames+" having size "+os.path.getsize(fnames))
        print(" ")

    print("************End of Folder****************")




def main():
    print("Directory watcher application")

    if (len(argv)<2):
        print("insuffucint argv")
        exit()
    if (argv[1]=="-h"):
        print("this script travel all dict")
        exit()

    if (argv[1] == "-u"):
        print("usage:application name")
        exit()

    dict_watcher(argv[1])


if __name__=="__main__":
    main()