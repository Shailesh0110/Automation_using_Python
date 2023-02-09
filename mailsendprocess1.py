from sys import *
import os
import hashlib
import time
import psutil
import urllib3
import smtplib,ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

def is_connected():
    try:
        urllib3.connection_from_url('http://216.58.192.142 ', timeout=1)
        return  True

    except Exception as E:
        print("Invalid Url:",E)


def Mail_sender(path):
    try:
        fromaddr = "shaileshnikam13@gmail.com"
        toaddr = 'marvellousinfosystem@gmail.com'
        subject = "Python automation Duplicate Delete file log file mail"
        body = """
        Hello ,
        wolcome to python automation script
        plsese find attched file.
        
        
        Thanks,
        Shailesh
        This is auto genertaed mail."""

        msg = MIMEMultipart()
        msg['from'] = fromaddr
        msg['to'] = toaddr
        msg['subject'] = subject

        msg.attach(MIMEText(body))

        files = path
        with open(files, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(files)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
            msg.attach(part)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            print('waiting to login...')
            server.login(fromaddr, '********')
            print('waiting to send...')

            server.send_message(msg, from_addr=fromaddr, to_addrs=[toaddr])

        print('email appears to have been sent with attchement')
    except Exception as E:
        print("unable to sent:",E)


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
        print("Duplicated deleted and keep the recod in log file")
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
    log_path = os.path.join(log_dir, "Marvellous%s.log" % (time.time()))
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

        connected=is_connected()
        if connected:
            starttime=time.time()
            Mail_sender(log_path)

            endtime=time.time()
            print("time take for Mail sende is %s"%(endtime-starttime))


    else:
        f.write("\n")
        f.write("**************Deleted files Not found **********************")
        print("Not Duplicate files found.")



def main(path):
    arr = {}
    startTime = time.time()
    arr = finduplicate(path)
    printduplicates(arr)
    Deletfile(arr)
    print("programe close succesfully")



