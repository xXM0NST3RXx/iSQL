from urllib.error import URLError, HTTPError
import urllib.request
from termcolor import *
import webbrowser
import sys

def adminfind(site):
	real=site.find("/",9)
	site=site.replace(site[real:],"/")

	with open("docs/paths.txt",mode="r+")as admnpath:
		for path in admnpath:
			print(colored("     Trying: ","grey")+site+path)
			try:
				opn=urllib.request.urlopen(site+path)
				print("       "+colored("[Admin page found]=>","blue","on_white")+"   "+site+path)
				webbrowser.open(site+path)
				break        
			except HTTPError as err:
				error = err.getcode
				if error== 404:
					continue
			except URLError as err:
				print(colored("Weak Connection or Bad broxy!!","yellow"))
			except:
				pass
