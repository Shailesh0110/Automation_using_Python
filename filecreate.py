
def create_file(filename):
    fd=open(filename,"w")
    fd.close()
def main():
    print("Enter the file name create")
    name= input()

    create_file(name)

if __name__=="__main__":
    main()