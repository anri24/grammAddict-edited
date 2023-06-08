import os 
import shutil
import subprocess as sp

username = input('what is your accounts username? ')
config_dir = 'accounts/'+username
config_ex = 'config-examples'
dest = 'accounts/'+username
config = os.path.exists(config_dir)

if(config == False):
    noAccountFile = input("There is no account's config file, do you want to create new ? (yes/no) ") 
    if (len(noAccountFile) > 0):
        answer = noAccountFile[0]
    if noAccountFile == '' or answer == "y":
        shutil.copytree(config_ex, dest) 
        print()
        print('config file is created go inside and chage other importent things ('+ dest +'/config.yml)')
        sp.Popen(["notepad.exe", dest +"/config.yml"])
    elif answer == "n":
        exit 
else:
    os.system('python run.py --config accounts/'+ username +'/config.yml')