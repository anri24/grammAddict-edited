import os 
import shutil
import subprocess as sp
import time

# openmemu = os.startfile(r"c:\Users\anriv\Desktop\MEmu-1.lnk")
# time.sleep(10)
username = input('what is your accounts username ? ')
config_dir = 'accounts/'+username
config_ex = 'config-examples'
config = os.path.exists(config_dir)

def askForChangeFile():
    print('------------------------')
    print("do you want to")
    print('1 -> check device address')
    print('2 -> change config file')
    print('3 -> change filter file')
    print('4 -> run')
    return input('-> ') 

def openFiles():
    changeConfig = askForChangeFile()
    while(changeConfig != 4):
        if changeConfig == '1':
            os.system('adb devices')
            changeConfig = askForChangeFile()
        elif changeConfig == '2':
            secondConf = sp.Popen(["notepad.exe", config_dir +"/config.yml"])
            secondConf.wait()
            changeConfig = askForChangeFile()
        elif changeConfig == '3':
            secondConf = sp.Popen(["notepad.exe", config_dir +"/filters.yml"])
            secondConf.wait()
            changeConfig = askForChangeFile()
        elif changeConfig == '4':
            os.system('python run.py --config '+ config_dir +'/config.yml')
    
    
if(config == False):
    noAccountFile = input("There is no account's config file, do you want to create new ? (yes/no) ") 
    if (len(noAccountFile) > 0):
        answer = noAccountFile[0]
    if noAccountFile == '' or answer == "y":
        shutil.copytree(config_ex, config_dir) 
        openFiles()
    elif answer == "n":
        exit 
else:
    openFiles()




