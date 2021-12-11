#import library 
import os
from colorama import Fore,init

#Show Welcome
os.system('clear')#clear all terminal
print(Fore.CYAN+'''
      -------------------------------
      Welcome To Mac Terminal in Linux
      _______________________________
      ''')#Typed Welcome ...\
          
continue12 = input('continue {Yes or No}')
if continue12.lower() =='yes':
    pass
elif continue12.lower() =='no':
    print('oky\N{Crying Face}')
    exit()
os.system('clear')
nameuser=os.getlogin()#get user name!
#True While
Adrsees = os.getcwd()#get addrsees
print(Fore.GREEN+nameuser+"@"+Fore.BLUE+Adrsees+"~ %")#print address and username
while True:

    
    Terminalcode = input(Fore.WHITE+'$')#get command
    Terminalcode = Terminalcode.lower()#lover code 
    if Terminalcode[:2]=='cd':
        
        os.system('clear')
        os.chdir(Terminalcode[2:])
        Adrsees = os.getcwd()#get addrsees
        print(Fore.GREEN+nameuser+"@"+Adrsees+"~ %")#print address and username
    elif Terminalcode =='clear':
        os.system('clear')
        Adrsees = os.getcwd()#get addrsees
        print(Fore.GREEN+nameuser+"@"+Adrsees+" ~ %")#print address and username
    elif Terminalcode == 'exit':
        os.system('clear')
        exit()
        
    elif Terminalcode =='cls':
        os.system('cls')
        Adrsees = os.getcwd()#get addrsees
        print(Fore.GREEN+nameuser+"@"+Adrsees)
    else:
        Adrsees = os.getcwd()#get addrsees
        
        print(Fore.WHITE+"")
        os.system(Terminalcode)
        print(Fore.WHITE+"")
