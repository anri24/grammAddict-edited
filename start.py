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
    changeConfig = input("do you want to change config file ? (yes/no) ") 
    if (len(changeConfig) > 0):
        answer = changeConfig[0]
    if changeConfig == '' or answer == "y":
        secondConf = sp.Popen(["notepad.exe", config_dir +"/config.yml"])
        secondConf.wait()
        os.system('python run.py --config '+ config_dir +'/config.yml')
    elif answer == "n":
        os.system('python run.py --config '+ config_dir +'/config.yml')
