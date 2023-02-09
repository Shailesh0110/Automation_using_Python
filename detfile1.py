import os
def del_file(filename):
    if (os.path.exists(filename)):
        size=os.path.getsize(filename)
        if size==0:
            os.remove(filename)
        else:
            print("are you sure delet file? y/n")
            option=input()
            if option=="y" or option=="Y":
                os.remove(filename)
                print("file succefully delet")
            else:
                print("file not delet")
    else:
        print("file is not existing")
def main():
    print("Enter the file name for delet")
    name = input()
    del_file(name)
if __name__ == "__main__":
    main()