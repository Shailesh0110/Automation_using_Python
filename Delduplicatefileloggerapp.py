from sys import *
import os
import hashlib
import time
import psutil


def Deletfile(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    i = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                i = i + 1
                if i >= 2:
                    os.remove(subresult)
                    i = 0
            print("Duplicated deleted")
    else:
        print(" ")


def hashfile(path, blocksize=1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buffer = fd.read(blocksize)
    while len(buffer) > 0:
        hasher.update(buffer)
        buffer = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()


def finduplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for foldername, subfolder, filname in os.walk(path):
            # print("Current folder is : " + foldername)
            for filen in filname:
                path = os.path.join(foldername, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")


def printduplicates(dict1, log_dir="marvellous"):
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "_" * 80
    log_path = os.path.join(log_dir, "Shailesh%s.log" % (time.time()))
    f = open(log_path, 'w')

    f.write(separator + "\n")
    f.write("Shailesh duplicate file systeem :" + (time.ctime()) + "\n")
    f.write(separator + "\n")

    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        i = 0
        for result in results:
            for subresult in result:
                i = i + 1
                if i >= 2:
                    f.write("%s\n" % subresult)
                    i = 0

        f.write("\n")
        f.write("**************Succesfully Deleted this files**********************")
        f.close()


    else:
        f.write("\n")
        f.write("**************Deleted files Not found **********************")
        print("Not Duplicate files found.")


def main():
    from sys import *
    import os
    import hashlib
    import time
    import psutil

    def Deletfile(dict1):
        results = list(filter(lambda x: len(x) > 1, dict1.values()))
        i = 0
        if len(results) > 0:
            for result in results:
                for subresult in result:
                    i = i + 1
                    if i >= 2:
                        os.remove(subresult)
                        i = 0
                print("Duplicated deleted")
        else:
            print(" ")

    def hashfile(path, blocksize=1024):
        fd = open(path, 'rb')
        hasher = hashlib.md5()
        buffer = fd.read(blocksize)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = fd.read(blocksize)
        fd.close()
        return hasher.hexdigest()

    def finduplicate(path):
        flag = os.path.isabs(path)
        if flag == False:
            path = os.path.abspath(path)

        exists = os.path.isdir(path)

        dups = {}

        if exists:
            for foldername, subfolder, filname in os.walk(path):
                # print("Current folder is : " + foldername)
                for filen in filname:
                    path = os.path.join(foldername, filen)
                    file_hash = hashfile(path)
                    if file_hash in dups:
                        dups[file_hash].append(path)
                    else:
                        dups[file_hash] = [path]
            return dups
        else:
            print("Invalid Path")

    def printduplicates(dict1, log_dir="marvellous"):

        if not os.path.exists(log_dir):
            try:
                os.mkdir(log_dir)
            except:
                pass

        separator = "_" * 80
        log_path = os.path.join(log_dir, "Shailesh%s.log" % (time.time()))
        f = open(log_path, 'w')

        f.write(separator + "\n")
        f.write("Shailesh duplicate file systeem :" + (time.ctime()) + "\n")
        f.write(separator + "\n")

        results = list(filter(lambda x: len(x) > 1, dict1.values()))
        if len(results) > 0:
            i = 0
            for result in results:
                for subresult in result:
                    i = i + 1
                    if i >= 2:
                        f.write("%s\n" % subresult)
                        i = 0

            f.write("\n")
            f.write("**************Succesfully Deleted this files**********************")
            f.close()


        else:
            f.write("\n")
            f.write("**************Deleted files Not found **********************")
            print("Not Duplicate files found.")

    def main():
        print("---- Marvellous Infosystems by Piyush Khairnar-----")

        print("Application name : " + argv[0])

        if (len(argv) != 2):
            print("Error : Invalid number of arguments")
            exit()

        if (argv[1] == "-h") or (argv[1] == "-H"):
            print("This Script is used to traverse specific directory")
            exit()

        if (argv[1] == "-u") or (argv[1] == "-U"):
            print("usage : ApplicationName AbsolutePath_of_Directory")
            exit()

        try:
            arr = {}
            startTime = time.time()
            arr = finduplicate(argv[1])
            printduplicates(arr)
            Deletfile(arr)

            endtime = time.time()
            print("Took %s seconds to evaluate." % (endtime - startTime))

        except ValueError:
            print("Error : Invalid datatype of input")

        except Exception as E:
            print("Error : Invalid input", E)

    if __name__ == "__main__":
        main()

    print("Application name : " + argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = finduplicate(argv[1])
        printduplicates(arr)
        Deletfile(arr)

        endtime = time.time()
        print("Took %s seconds to evaluate." % (endtime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input", E)


if __name__ == "__main__":
    main()