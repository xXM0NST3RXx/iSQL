from googlesearch import *
from docs.cheaker import *
def googlesrchers(filename,serchword,choice2):
	for url in search(serchword,stop=150):
		print(url)
		with open(filename,mode="a")as typer:
			typer.write(url+"\n")
		cheaker(url,choice2)
