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
    print('1 -> change config file')
    print('2 -> change filter file')
    print('3 -> run')
    return input('-> ') 
    

if(config == False):
    noAccountFile = input("There is no account's config file, do you want to create new ? (yes/no) ") 
    if (len(noAccountFile) > 0):
        answer = noAccountFile[0]
    if noAccountFile == '' or answer == "y":
        shutil.copytree(config_ex, config_dir) 
        firstConf = sp.Popen(["notepad.exe", config_dir +"/config.yml"])
        firstConf.wait()        
        os.system('python run.py --config '+ config_dir +'/config.yml')
    elif answer == "n":
        exit 
else:
    changeConfig = askForChangeFile()
    while(changeConfig != 3):
        if changeConfig == '1':
            secondConf = sp.Popen(["notepad.exe", config_dir +"/config.yml"])
            secondConf.wait()
            changeConfig = askForChangeFile()
        elif changeConfig == '2':
            secondConf = sp.Popen(["notepad.exe", config_dir +"/filters.yml"])
            secondConf.wait()
            changeConfig = askForChangeFile()
        elif changeConfig == '3':
            os.system('python run.py --config '+ config_dir +'/config.yml')




