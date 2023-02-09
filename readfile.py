import os

def read_file(filename):
    if (os.path.exists(filename)):
        fd = open(filename, "r")
        data= fd.read()
        print("Data from the file is ")
        print(data)

        fd.close()
    else:
        print("file is not existing")
        return

def main():
    print("Enter the file name create")
    name = input()

    read_file(name)

if __name__ == "__main__":
    main()