#!/usr/bin/python3
#
#org_zero: Pain :https://www.facebook.com/ThePainX
#MrMax:https://www.facebook.com/Mr0max
#Elsafa7-110:https://www.facebook.com/elsfa7110
#Teto:https://www.facebook.com/XxtetogenXx
#Twix: https://www.facebook.com/Twix17
#Sniper-UMS(Co-Creator): https://www.facebook.com/profile.php?id=100006450001579
#M0NST3R(Creator):https://www.facebook.com/leave0me0here.py
#Striker:https://www.facebook.com/StrikerHacker33
#
#
import os,sys,time,datetime #bult-in libs
os.system("clear")
try:
    from termcolor import *
except ImportError:
    print("You don't have 'termcolor' module trying to install!!")
    os.system("pip3 install termcolor")
    
if os.getuid() != 0:
    print("\n"+'\033[1m'+colored("[Run the code as root]","red")+'\n')
    os.system("clear");print("\n"+'\033[1m'+colored("[Run the code as root]","red").center(85,"-")+'\n');print("Exiting.");time.sleep(1);os.system("clear");print("\n"+'\033[1m'+colored("[Run the code as root]","red").center(85,"-")+'\n');print("Exiting..");time.sleep(1);os.system("clear");print("\n"+'\033[1m'+colored("[Run the code as root]","red").center(85,"-")+'\n');print("Exiting...");time.sleep(1)
    sys.exit()
    
	
try:
    from googlesearch import *
except ImportError:
    print(colored("You don't have google module trying to install!!","red"))
    os.system("pip3 install google")
import docs.bing_search
import docs.cheaker
import docs.proxies
import docs.adminfinder
import docs.dorkgen
import docs.googlesearcher
print(colored('''
                               ....                                         
                                    %                                       
                                     ^                                      
                            L                                               
                            "F3  $r                                         
                           $$$$.e$"  .                                      
                           "$$$$$"   "                                      
                            .$$$$c  /                                       
        .                   $$$$$$$P                                        
       ."c                      $$$                                         
      .$c3b                  ..J$$$$$e                                      
      4$$$$             .$$$$$$$$$$$$$$c                                    
       $$$$b           .$$$$$$$$$$$$$$$$r                                   
          $$$.        .$$$$$$$$$$$$$$$$$$                                   
           $$$c      .$$$$$$$  "$$$$$$$$$r                                  
            $$$b    .$$$$ $$$"^b $$$$$$$$$                                  
             *$$$   $$$$  $$P4$ $^$$$$ $$$                                  
              *$$$.$$$$   4$b'$$$.3$$P *$$F                                 
               "$$$$$P    4$$e."$$$$$%  $$$                                 
                "$$$P      $$$$b $$$$   *$$                                 
                  ""       $$$$$$."$$$c  $$F                                
                           $$$$$$$e $$$$.*$$                                
                .ee.       $$$$$$$$$  *$$$$$                                
               4$$  ^b     $$$$$$$$$   ^$$$$                                
               $$$    ^c   $$$$$$$$F     "*$%                               
               3$$c     *  $$$$*"""F                                        
                $$$$      cP"                                               
                ^$$$$c .e"                                                  
                 ^$$$$"                                                     
                  JP"                                                       
                e"                '                                         
              d$                  %z.                                       
             $$$                  $$$c                                      
           z$$$$eeeeeeeeeeeeeeeeed$$$$e                                     
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                  
           """"""""""""""""""""""""""""""""
		 _ _____ _____ __    
		|_|   __|     |  |   
		| |__   |  |  |  |__ 
		|_|_____|__  _|_____|
			   |__|      
''',"cyan"))
print("     		 "+colored("Egy","red","on_yellow")+colored("pt","white","on_yellow")+colored("ian","grey","on_yellow")+colored(" Made 3>","magenta"))
print("\nCoded BY: "+colored("M0NSTƎR","yellow")+" & "+colored("Sniper-UMS\n","cyan"))
print(colored(" @0RG4NIZ4TI0N-Z3R0 ","red").center(70,"#"))
print(" Zero No One ".center(70,"#"))

print(colored("do you want to use the tool using proxychains (Y,n) ??(ADVICED): ","blue"))
choiser3=input("iSQL@root:~$ ")
if choiser3 == "Y" or choiser3 == "y": 
	print(colored("enter the proxies file(.txt)","blue"))
	prxyfile=input("iSQL@root:~$ ")
	docs.proxies.proxier(prxyfile)
	print(colored("Run The script again using proxychains by typing (proxychains sudo iSQL.py) and choose (N) when the proxy option shows ","red"))
	sys.exit()
print(colored("Enter dork or enter file path(.txt files only) (leave empty if you want to generate Dorks)","blue"))
enterdorks=""+input("iSQL@root:~$ ")
print(colored("Do you want to find admin for exploitable sites? : (y,n)","blue"))
choice2=input("iSQL@root:~$ ")
dorkfilename=str(datetime.datetime.now().isoformat().replace(":","_"))+".txt"
if enterdorks=="":
	print(colored("Enter Numbers of Dorks You want to get from (cxsecurity.com)","blue"))
	amount=input("iSQL@root:~$ ")
	print(colored("Do you want to generate some sql dorks with your keyword? (y,n)","blue"))
	chooser=input("iSQL@root:~$ ")
	if chooser == "y" or chooser == "Y":
		print(colored("Enter KeyWord","blue"))
		word=input("iSQL@root:~$ ")
	else:
		word="n"
		
	docs.dorkgen.dorker(dorkfilename,amount,chooser,word)
	enterdorks="Dorks"+dorkfilename
	
filename=time.strftime("%d/%m/%Y").replace("/","_")+"_"+str(time.time()).replace(".","_")

with open(filename,mode="w+")as typer:
    typer.write("")
if enterdorks[len(enterdorks)-3:len(enterdorks)]=="txt":
			with open(enterdorks,mode="r+") as dorks:
				lines=dorks.readlines()
				for line in lines:
					serchword=line.replace("\n","")
					docs.bing_search.bing(filename,serchword,choice2)
					docs.googlesearcher.googlesrchers(filename,serchword,choice2)
else :
	docs.bing_search.bing(filename,enterdorks,choice2)
	docs.googlesearcher.googlesrchers(filename,enterdorks,choice2)


