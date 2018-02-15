import bs4
import urllib.request as req
from urllib.error import URLError, HTTPError
import datetime
from termcolor import *
def dorker(now,amount,chooser,word):
    drknumber=1
    with open("Dorks"+str(now),"w+")as dorks:
        dorks.write("")
    if int(amount) <= 25:
        amount=25
    while drknumber*20 < int(amount)*2:
        try:
            url=req.urlopen("https://cxsecurity.com/dorks/"+str(drknumber)).read()
            soap=bs4.BeautifulSoup(url,'html.parser')
        except URLError as err:
                    print(colored("You may had panned from cxsecurity.com try using proxy!!","yellow"))
                    print(colored("Trying again !!","cyan"))
        obj=soap.find_all("td")
        drknumber=drknumber+1
        for span in obj:
            for h6 in span.find_all("h6"):
                a=str(h6)
                a=a.replace("<h6><b>Dork:</b> ","")
                a=a.replace("</h6>","")
                if a.startswith("<h6><span") == True:
                    continue
                print(a)
                try:
                    with open("Dorks"+str(now),"a")as dorks:
                        dorks.write(a+"\n")
                except UnicodeEncodeError:
                    pass
                except:
                    pass
    ########################Dork_GENERATOR#################################
    print(colored("Jop Finished!!","green"))
    if chooser == "y" or chooser=="Y":
        #word=input("Enter KeyWord : ")
        l=["id=","category=","Pageid=","index=","title=","topic=","list=","GameID=","game=","showtopic=","item=","newsid=","GameCode=","id_product=","gametype=","detail=","idPage=","jobid=","topic=","langid="]
        l2=[".php?",".asp?",".html?",".cgi?",".aspx?",".cfm?"]
        for item in l:
            for item1 in l2:
                print("inurl:"+word+item1+item)
                with open("Dorks"+str(now),mode="a")as f:
                    f.write("inurl:"+word+item1+item+"\n")
                path=os.getcwd()
        print("Dorks Saved in  "+path+"/"+str(now)+"\n")
        print(colored(" [Search Started] ","cyan").center(70,"-"))

    else :
        print(colored(" [Search Started] ","cyan").center(70,"-"))
        with open("Dorks"+str(now),mode="a")as f:
            f.write(" ")
