from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
KW = input("Enter Item to be searched of Amazon.in: ")
URL = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + KW
uCLient = uReq(URL)
html = uCLient.read()
uCLient.close()
Filename = KW+".csv"
fp = open(Filename,"w")
headers = "Model,Price,Rating\n"
fp.write(headers)
page_soup = soup(html, "html.parser")
Containers = page_soup.findAll("div",{"class":"s-item-container"})
print("Creating Database for",len(Containers),"items...")
for Container in Containers[1:]: #Each container has details of the item searched 
    str = Container.div.text
    Model = str.split("by")
    Price = Model[1].split('\xa0')
    Price = Price[2]
    Price = re.findall(r'[0-9]*[,][0-9]*',Price)
    Price = Price[0]
    Model = Model[0]
    tmp = str.split("stars")
    tmp = tmp[0].split(" ")
    tmp = tmp[len(tmp) - 5].split("\n")
    tmp = tmp[len(tmp) - 1]    
    if (re.findall(r'[0-9][.][0-9]',tmp)):
        Ratings = tmp
    else:
        Ratings = "N/A"
    fp.write(Model.replace(",", " ") + "," + Price.replace(",", " ") + "," + Ratings + "\n")
fp.close()