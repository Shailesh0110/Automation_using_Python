import psutil

def Display_procss():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            printinfo=proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(printinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def main():
    print("*********marvellous infosysteem:python Automation************")

    print("Process Monitor")

    list=Display_procss()

    for i in list:
        print(i)

if __name__=="__main__":
    main()