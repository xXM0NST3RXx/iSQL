from googlesearch import *
from docs.cheaker import *
from urllib.error import URLError, HTTPError
def googlesrchers(filename,serchword,choice2):
	try:
		for url in search(serchword,stop=150):
			print(url)
			with open(filename,mode="a")as typer:
				typer.write(url+"\n")
	except:
		print("You Brobaly banned from google :/ \n why you don't use broxychains")
		pass
		cheaker(url,choice2)
