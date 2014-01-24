#-------------------------------------------------------

#TijnUtility
#written for python 2.7.5
#If you use this program on a Raspberry Pi you should uncomment the code where stands #RPi only
#You can disable functions to put a # before it by the cmdline function
#Made by: Tijndagamer
#Published under the GPL v2 licence
#for more info email to: tijndagamer25@gmail.com

#copyright Tijndagamer 2014

#-------------------------------------------------------

#DISCLAIMER:
#Everywhere in this program where is said "infinte amount of spaces". These spaces are LIMITID by the computer YOU use it on.
#Please note that the login function IS NOT 100% secure

#-------------------------------------------------------

#importing needed libs.
import time
import random
import pickle
import os
import shutil
import socket
import sys
import smtplib
import poplib
from datetime import datetime

#-------------------------------------------------------

#Config, You can config TijnUtility here, to disable functions see the cmdline function
eMailAddr = "@gmail.com"#your email address (gmail only)
eMailPass = ""#your email password (please be aware that this is not encrypted)

#-------------------------------------------------------

#welcoming script:
print(">Welcome to TijnUtility version 0.4")
time.sleep(0.5)
print(">to save the data use the save command, type help if you need help")
time.sleep(0.5)

#-------------------------------------------------------

#importing the data stored in the intbyte.TijnUtility and strbyte.TijnUtility

intbyte = pickle.load(open("intbyte.TijnUtility", "rb"))
strbyte = pickle.load(open("strbyte.TijnUtility", "rb"))

#-------------------------------------------------------

#Write functions

def writeintbyte():
        input = raw_input(">input =")
        intbyte.append(int(input))
def writestrbyte():
        input = raw_input(">input =")
        strbyte.append(str(input))

#-------------------------------------------------------

#Read Functions

def readintbyte():
        print intbyte
def readstrbyte():
        print strbyte

#-------------------------------------------------------

#Math functions

def extractintbyte():
        x = raw_input(">x =")
        y = raw_input(">y =")
        answer = int(x) - int(y)
        intbyte.append(int(answer))
        print(answer)
def addintbyte():
        x = raw_input(">x =")
        y = raw_input(">y =")
        answer = int(x) + int(y)
        intbyte.append(int(answer))
        print(answer)
def multiplyintbyte():
        x = raw_input(">x =")
        y = raw_input(">y =")
        answer = int(x) * int(y)
        intbyte.append(int(answer))
        print(answer)
def divideintbyte():
        x = raw_input(">x =")
        y = raw_input(">y =")
        answer = int(x) / int(y)
        intbyte.append(int(answer))
        print(answer)
def topowerintbyte():
        print("Be carefull with high numbers, it might crash the program or your computer")
        x = raw_input(">x =")
        y = raw_input(">y =")
        answer = int(x) ** int(y)
        intbyte.append(int(answer))
        print(answer)

#-------------------------------------------------------

#Utility functions

def date():
        now = datetime.now()
        print(now)
def randomintintbyte():
        randomint = random.randint(-99999999999999999999,99999999999999999999)
        print(randomint)
        intbyte.append(int(randomint))
def htmlgen():
        print("<html>")
        print("<head>")
        print('<link type="text/css" rel="stylesheet" href="stylesheet.css"/>')
        print("<title></title>")
        print("</head>")
        print("<body>")
        print("<h1></h1>")
        print("<h4></h4>")
        print("<p></p>")
        print("</body>")
        print("</html>")
def TijnUtilityhelp():
        print("These are all the commands that are available now:")
        print("writeintbyte #to write an integer in the integer storage list")
        print("writestrbyte #to write a string in the string storage list")
        print("readintbyte #prints the data stored in the integer storage list")
        print("readstrbyte #prints the data stored in the string storage list")
        print("extract #asks for two numbers to make a sum of them. it prints the answer and stores the answer in the integer storage list.")
        print("add #asks for two numbers to make a sum of them. it prints the answer and stores the answer in the integer storage list.")
        print("multiply #asks for two numbers to make a sum of them. it prints the answer and stores the answer in the integer storage list.")
        print("divide #asks for two numbers to make a sum of them. it prints the answer and stores the answer in the integer storage list.")
        print("topower #asks for two numbers to make a sum of them. it prints the answer and stores the answer in the integer storage list.")
        print("date #prints the date")
        print("randomint #generates a random integer and prints it and stores it in the integer storage list.")
        print("randomword #chooses one of the words in it's database prints it and stores it in the string storage list")
        print("htmlgen #prints the basic structure of a HTML/PHP page")
        print("resetintbyte #deletes the last integer in the integer storage list")
        print("resetstrbyte #deletes the last string in the string storage list")
        print("rpsc #starts a game of rock, paper, scissors against the computer")
        print("lottery #a fun game")
        print("save #saves the data")
        print("catstrbyte #prints a specific index of the string storage list")
        print("catintbyte #prints a specific index of the integer storage list")
        print("newfile #makes a new file")
        print("loadfile #loads a file")
        print("editfile #edit a file")
        print("rpsp #starts a game of rock, paper, scissors against an other person")
        print("removefile #removes a file")
        print("copyfile #copies a file")
        print("connectIPrecv #connects to a socket server and receives information")
        print("connectIPsend #connects to a socket server and sends information")
        print("connectIPrecvsend #connects to a socket server and receives and sends informtaion")
        print("HostSend #hosts a socket server and sends information to all the clients that are connected")
        print("HostRecv #hosts a socket server and receives information from all the clients that are connected")
        print("HostSendRecv #hosts a socket server and sends and receives information from all the clients that are connected")
        print("shutdown #shutsdown TijnUtility")
        print("emailsend #sends an email")
        print("emailcheck #checks if you have configurated your email address and password correct")
        print("emailsendfile #sends a file using email")
        print("emailrecv #lets you receive an email")
        print("emailspam #sends a by user givin amount of emails to the target address")
        print("sysls #executes the ls command in the main cmdline of the RPi")
        print("reboot #reboots the RPi")
        print("wget, aptget and python #same as the normal cmdline in your RPi")
        print("emailsendtemp #sends the temp of the proccesor of the RPi in an email")

#-------------------------------------------------------

#Game functions

def lottery():
        lot = random.randint(0,99)
        choice = raw_input(">Which number do you choose?(between 0 and 99)")
        print("Your choice is: " + choice)
        if lot == choice:
                print("The winning number is:")
                print(choice)
                print("You win!!")
        else:
                print("The computer choose")
                print(lot)
                print("You lost....")
def rpsc():
        user = raw_input(">What do you choose?")
        computer = random.randint(0, 2)
        if user == "rock":
                if computer == 0:
                        print("It's a tie!")
                if computer == 1:
                        print("The computer choose paper, you've lost...")
                if computer == 2:
                        print("The computer choose scissors, you won!!")
        if user == "paper":
                if computer == 1:
                        print("It's a tie!")
                if computer == 2:
                        print("The computer choose scissors, you've lost...")
                if computer == 0:
                        print("The computer choose rock, you won!!")
        if user == "scissors":
                if computer == 2:
                        print("It's a tie!")
                if computer == 0:
                        print("The computer choose rock, you've lost...")
                if computer == 1:
                        print("The computer choose paper, you won!!")
def rpsp():
        user1 = raw_input(">What do you choose?")
        user2 = raw_input(">And what do you choose?")
        if user1 == "rock":
                if user2 == "rock":
                        print("It's a tie!")
                if user2 == "paper":
                        print("user2 choose paper, you've lost...")
                if user2 == "scissors":
                        print("user2 choose scissors, you won!!")
        if user1 == "paper":
                if user2 == "paper":
                        print("It's a tie!")
                if user2 == "scissors":
                        print("user2 choose scissors, you've lost...")
                if user2 == "rock":
                        print("user2 choose rock, you won!!")
        if user1 == "scissors":
                if user2 == "scissors":
                        print("It's a tie!")
                if user2 == "rock":
                        print("user2 choose rock, you've lost...")
                if user2 == "paper":
                        print("user2 choose paper, you won!!")
def ping():
        print(">pong!")
def dance():
        danceTime = raw_input(">How long? (in seconds) ")
        loopEnd = int(danceTime) * 5
        i = 0
        while i < loopEnd:
                move = random.choice([
                        "<('_'<) ^('_')^ (>'_')>",
                        "\('.')/ \('.')\ /('.')/",
                        "~('_.)~ ~(._')~ ~('_')~",
                        "^('-')^ ^('~')^ ^('=')^",
                        "\(@.@)\ /(@.@)/ \(@.@)\ ",
                ])
                print move
                time.sleep(0.2)
                i = i + 1
        #The new dance function is made by: Pietdagamer

#-------------------------------------------------------

#File functions

def save():
        pickle.dump(intbyte, open("intbyte.TijnUtility", "wb"))
        pickle.dump(strbyte, open("strbyte.TijnUtility", "wb"))
        print("Lists saved!")
def ls():
        print("intbyte:")
        print(intbyte)
        print("strbyte:")
        print(strbyte)
def catstrbyte():
        index = raw_input(">Which index?")
        print(strbyte[int(index)])
def catintbyte():
        index = raw_input(">Which index?")
        print(intbyte[int(index)])
def resetintbyte():
        a = raw_input(">Which index?")
        intbyte.pop(int(a))
        print("Done!")
def resetstrbyte():
        a = raw_input(">Which index?")
        strbyte.pop(int(a))
        print("Done!")
def newfile():
        filename = raw_input(">name =")
        fileinput = raw_input(">input =")
        pickle.dump(fileinput, open(filename, "wb"))
def loadfile():
        filetoload = raw_input(">file =")
        loaded_file = pickle.load(open(filetoload, "rb"))
        print(loaded_file)
def editfile():
        filetoedit = raw_input(">file =")
        a = pickle.load(open(filetoedit, "rb"))
        print("This is now in the file: " + a)
        change = raw_input(">input =")#remember that everything gets overwritten
        pickle.dump(change, open(filetoedit, "wb"))
def removefile():
        filetoremove = raw_input(">file =")
        os.remove(filetoremove)
        print("File is removed")
def copyfile():
        src_input = raw_input(">source =")
        dst_input = raw_input(">destination =")
        shutil.copy(str(src_input), str(dst_input))
        print("File is copied succesfully")

#-------------------------------------------------------

#System functions

def shutdown():
        sure = raw_input(">Are you sure you want to shutdown?y/n")
        if sure == "y":
                print("System shutdown in: 3")
                time.sleep(1)
                print("System shutdown in: 2")
                time.sleep(1)
                print("System shutdown in: 1")
                time.sleep(0.9)
                print("System shutdown in: NOW")
                time.sleep(0.1)
                sys.exit()
        else:
                print("Shudown cancelled")

#-------------------------------------------------------

#Networking client functions (requires an internet connection)

def connectIPrecv():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = raw_input(">host =")
        port = int(raw_input(">port ="))
        s.connect((host, port))
        data = s.recv(1024)
        print(data)
        time.sleep(0.1)
        yayornay = raw_input("Save data to strbyte?y/n")
        if yayornay == "y":
                savedata = "Saved message : " + data
                strbyte.append(str(savedata))
                time.sleep(0.1)
                print("Data is saved")
        else:
                print("Data is not saved")
        time.sleep(0.5)
        s.close()
        print("Connection closed")
def connectIPsend():
        host = raw_input(">host =")
        port = int(raw_input(">port ="))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Succesfully connected to " + host)
        msg = raw_input(">msg =")
        s.send(msg)
        s.close()
        print("Connection closed")
def connectIPrecvsend():
        host = raw_input(">host =")
        port = int(raw_input(">port ="))
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        print("Succesfully connected to " + host)
        recv = s.recv(1024)
        print(recv)
        msg = raw_input(">msg =")
        s.send(msg)
        print("Connection closed")
        yayornay = raw_input("Save data to strbyte?y/n")
        if yayornay == "y":
                savedata = "Saved message : " + recv
                strbyte.append(str(savedata))
                time.sleep(0.1)
                print("Data is saved")
        else:
              print("Data is not saved")
        time.sleep(0.5)
        s.close()
        print("Connection closed")

#-------------------------------------------------------

#Networking server functions (requires an internet connection)
def HostSend():
        msg = raw_input(">msg =")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = int(raw_input(">port ="))
        s.bind((host, port))

        s.listen(5)
        while True:
                c, addr = s.accept()
                print("Got connection from", addr)
                c.send(msg)
                c.close
                print("Connection with " + str(addr) + ", is closed")
                break
def HostRecv():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = int(raw_input(">port ="))
        s.bind((host, port))

        s.listen(5)
        while True:
                c, addr = s.accept()
                print("Got connection from", addr)
                buf = c.recv(1024)
                if len(buf)> 0:
                        print buf
                c.close()
                print("Connection with " + str(addr) + ", is closed")
                break
def HostSendRecv():
        msg = raw_input(">msg =")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = int(raw_input(">port ="))
        s.bind((host, port))

        s.listen(5)
        while True:
                c, addr = s.accept()
                print("Got connection from", addr)
                c.send(msg)
                buf = c.recv(1024)
                if len(buf)> 0:
                        print(buf)
                c.close()
                print("Connection with " + str(addr) + ", is closed")
                yayornay = raw_input("Save data to strbyte?y/n")
                if yayornay == "y":
                        savedata = "Saved message : " + recv
                        strbyte.append(str(savedata))
                        time.sleep(0.1)
                        print("Data is saved")
                else:
                        print("Data is not saved")
                time.sleep(0.5)
                break

#-------------------------------------------------------

#Email functions (requires an internet connection)

def emailcheck():
        if eMailAddr == "@gmail.com" or "":
            print("Email address isn't configurated, please add you email address and password. Otherwhise you CAN NOT use any of the email functions.")
            cmdline()
        else:
                return True
                if eMailPass == "":
                        print("Email password isn't configurated, please add you email address and password. Otherwhise you CAN NOT use any of the email functions.")
                        cmdline()
                else:
                        return True
def emailsend():
        emailcheck()
        toAddr = raw_input(">Receiver address =")
        subject = raw_input(">Subject =")
        header = "To: " + toAddr + "\n" + "From: " + eMailAddr + "\n\n" + "Subject: " + subject
        body = raw_input(">Body =")
        print("Your email is:")
        print(header + "\n" + body)
        time.sleep(0.5)
        print("Please wait, this may take a while")
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(eMailAddr, eMailPass)
        s.sendmail(eMailAddr, toAddr, header + "\n" + body)
        s.quit
        print("Email is sent succesfully")
def emailsendfile():
        emailcheck()
        toAddr = raw_input(">Receiver address=")
        sendfile = raw_input(">file to send=")
        a = pickle.load(open(sendfile, "rb"))
        print("Your email is:" + "\n" + a)
        sure = raw_input(">Are you sure you want to send this email?y/n")
        if sure == "y":
                print("Please wait, this may take a while")
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(eMailAddr, eMailPass)
                s.sendmail(eMailAddr, toAddr, a)
                s.quit
                print("Email is sent succesfully")
        else:
                print("Email sending is cancelled")
def emailspam():
        emailcheck()
        toAddr = raw_input(">Target address=")
        msg = raw_input(">Message =")
        spamcount = raw_input(">Times sending =")
        header = "To: " + toAddr + "\n" + msg
        print("Your spam message is:")
        print header + "\n" + msg
        time.sleep(0.1)
        print("Please wait, this may take a while")
        i = 0
        while i < int(spamcount):
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(eMailAddr, eMailPass)
                s.sendmail(eMailAddr, toAddr, header + "\n\n" + msg)
                s.quit
                i = i + 1
                print(str(i) + " messages sent")
def emailrecv():
        emailcheck()
        a = raw_input(">which number?")
        print("Please wait, this may take a while")
        m = poplib.POP3_SSL("pop.gmail.com", 995)
        m.user(eMailAddr)
        m.pass_(eMailPass)
        msg = ""
        for i in m.retr(int(a))[1]:
                msg += i
        m.quit()
        print(msg)

#-------------------------------------------------------

#Raspberry Pi only functions

def temp():
        temp_measure = os.popen("/opt/vc/bin/vcgencmd measure_temp")
        temp = temp_measure.read()
        print(temp)
        strbyte.append(str(temp))

def reset():
        sure = raw_input(">Are you sure you want to reset?y/n")
        if sure == "y":
                os.system("python TijnUtility_files_generator.py")
                print("After a reboot the lists are reset")
        else:
               print("Reset cancelled")
def HostSendTemp(): #(requires an internet connection)
        temp = temp()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = int(raw_input(">port ="))
        s.bind((host, port))

        s.listen(5)
        while True:
                c, addr = s.accept()
                print("Got connection from", addr)
                c.send(temp)
                c.close
                print("Connection with " + str(addr) + ", is closed")
                break
def fullyshutdown():
        sure = raw_input(">Are you sure you want to shutdown?y/n")
        if sure == "y":
                print("System shutdown in: 3")
                time.sleep(1)
                print("System shutdown in: 2")
                time.sleep(1)
                print("System shutdown in: 1")
                time.sleep(0.9)
                print("System shutdown in: NOW")
                time.sleep(0.1)
                os.system("python /home/pi/TijnUtility/shutdown.py")
                sys.exit()
        else:
                print("Shutdown cancelled")
def sysls():
        ls = os.popen("ls")
        lsr = ls.read()
        print(lsr)
def reboot():
        sure = raw_input(">Are you sure you want to shutdown?y/n")
        if sure == "y":
                print("Bye!")
                time.sleep(0.1)
                os.system("sudo reboot")
        else:
                print("Reboot cancelled")
def emailsendtemp():
        emailcheck()
        temp = temp()
        toAddr = raw_input(">Receiver address =")
        subject = raw_input(">Subject =")
        header = "To: " + toAddr + "\n" + "From: " + eMailAddr + "\n\n" + "Subject: " + subject
        body = temp
        print("Your email is:")
        print(header + "\n" + body)
        time.sleep(0.5)
        print("Please wait, this may take a while")
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(eMailAddr, eMailPass)
        s.sendmail(eMailAddr, toAddr, header + "\n" + body)
        s.quit
        print("Email is sent succesfully")
        

#-------------------------------------------------------

#Commandline function

#to disable a command you should make a comment of it. e.g:
##if command == "command":
##       command()
def cmdline():
        count = 0
        while count < 2:
                command = raw_input(">")
                if command == "writeintbyte":#1
                        writeintbyte()
                if command == "readintbyte":#2
                        readintbyte()
                if command == "writestrbyte":#3
                        writestrbyte()
                if command == "readstrbyte":#4
                        readstrbyte()
                if command == "extract":#5
                        extractintbyte()
                if command == "add":#6
                        addintbyte()
                if command == "multiply":#7
                        multiplyintbyte()
                if command == "divide":#8
                        divideintbyte()
                if command == "date":#9
                        date()
                if command == "randomint":#10
                        randomintintbyte()
                if command == "randomword":#11
                        randomwordstrbyte()
                if command == "resetintbyte":#12
                        resetintbyte()
                if command == "resetstrbyte":#13
                        resetstrbyte()
                if command == "htmlgen":#14
                        htmlgen()
                if command == "topower":#15
                        topowerintbyte()
                if command == "ls":#16
                        ls()
                if command == "help":#17
                      TijnUtilityhelp()
                if command == "lottery":#18
                        lottery()
                if command == "rpsc":#19
                        rpsc()
                if command == "save":#20
                        save()
                if command == "catstrbyte":#21
                        catstrbyte()
                if command == "catintbyte":#22
                        catintbyte()
                if command == "newfile":#23
                        newfile()
                if command == "loadfile":#24
                        loadfile()
                if command == "ping":#25
                        ping()
                if command == "editfile":#26
                        editfile()
                if command == "dance":#27
                        dance()
                if command == "rpsp":#28
                        rpsp()
        #       if command == "temp":#29 #RPi only
        #               temp()
                if command == "removefile":#30
                        removefile()
                if command == "copyfile":#31
                        copyfile()
                if command == "connectIPrecv":#32
                        connectIPrecv()
                if command == "shutdown":#33
                        shutdown()
        #        if command == "reset":#34 #RPi only
        #                reset()
                if command == "connectIPsend":#35
                        connectIPsend()
                if command == "connectIPrecvsend":#36
                        connectIPrecvsend()
                if command == "HostSend":#37
                        HostSend()
                if command == "HostRecv":#38
                        HostRecv()
                if command == "HostSendRecv":#39
                        HostSendRecv()
        #       if command == "HostSendTemp":#40 #RPi only
        #               HostSendTemp
        #       if command == "fullyshutdown":#41 #RPi only
        #               fullyshutdown()
        #       if command == "sysls":#42 #RPi only
        #               sysls()
        #       if command == "python":#43 #RPi only
        #               python()
        #       if command == "reboot":#44 #RPi only
        #               reboot()
        #       if command == "wget":#45 #RPi only
        #               wget()
        #       if command == "aptget":#46 #RPi only
        #               aptget()
                if command == "emailsend":#47
                        emailsend()
                if command == "emailsendfile":#48
                        emailsendfile()
                if command == "emailspam":#49
                        emailspam()
                if command == "emailrecv":#50
                        emailrecv()
                if command == "emailcheck":#51
                        emailcheck()
        #       if command == "emailsendtemp":#52 #RPi only
        #               emailsendtemp()

#-------------------------------------------------------

cmdline()

