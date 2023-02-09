import os


def write_file(filename):
    if (os.path.exists(filename)):
        print("enter the data that you want to write")
        data = input()

        fd = open(filename, "a")
        fd.write((data))

    else:
        print("file is not existing")
        return


def main():
    print("Enter the file name create")
    name = input()

    write_file(name)


if __name__ == "__main__":
    main()