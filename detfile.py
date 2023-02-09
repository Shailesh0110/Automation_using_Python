import os


def del_file(filename):
    if (os.path.exists(filename)):

        os.remove(filename)


    else:
        print("file is not existing")



def main():
    print("Enter the file name for delet")
    name = input()

    del_file(name)


if __name__ == "__main__":
    main()