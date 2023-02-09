import os

def create_file(filename):

    if (os.path.exists(filename)):
        print("already exist")
    else:
        fd = open(filename, "w")


def main():
    print("Enter the file name create")
    name= input()


    create_file(name)

if __name__=="__main__":
    main()