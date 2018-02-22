from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse , docs.cheaker
from urllib.request import Request

def bing(filename,word,choice2):
    pagenumber=11
    sites_list=[]
    while pagenumber <= 561:
        try:
            search={"q":word}
            seachencode=urllib.parse.urlencode(search)
            url=Request("http://www.bing.com/search?"+seachencode+"&go=Submit+Query&qs=ds&first="+str(pagenumber)+"&FORM=PERE",headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"})
            urlopen=req.urlopen(url)
            html_content=urlopen.read(5000000)
            soup=BeautifulSoup(html_content,"html.parser")
            for link in soup.find_all("h2",{"class":""}):
                try:
                    site=link.a.get("href")
                    if site not in sites_list:
                        sites_list.append(site)
                        with open(filename,mode="a")as typer:
                            typer.write(site+"\n")
                        print(site)
                        docs.cheaker.cheaker(site,choice2)
                    else :
                        pass
                except AttributeError:
                    pass
            pagenumber=pagenumber+11
        except:
            pass
            pagenumber=pagenumber+11
    
