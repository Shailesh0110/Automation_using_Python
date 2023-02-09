from sys import *

def add(A,B):
    ans=0
    ans=A+B
    return  ans

def main():
    print('Welcome  to : ', argv[0])

    if (len(argv)==2):
        if (argv[1]=="--U"):
            print('Use the application as:')
            print("Python name of application first and second no.")
            exit()

        if (argv[1]=="--H"):
            print("Help: this app is used for 2 no.s Addition")
            exit()


    if (len(argv)!=3):
        print('invalied sentance')
        print("Please use --U flag to get the usages")
        exit()

    Ret=add(int(argv[1]),int(argv[2]))
    print("Addition is :", Ret)
    print('Thank yoy for using this application')
    print("Application is devloped by Shailesh Nikam")

if __name__ == "__main__":
        main()