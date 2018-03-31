from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
KW = input("Enter the item to be searched on Amazon.in: ")
URL = "https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + KW
uCLient = uReq(URL) #urllib.request.urlopen()
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
    str = Container.div
    Model = Container.div.div.img['alt']
    tmp = (Container.findAll("span",{"class":"a-size-base a-color-price a-text-bold"}))
    if tmp == []:
        tmp = Container.findAll("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
    Price = tmp[0].text
    tmp = Container.findAll("span",{"class":"a-icon-alt"})
    for items in tmp:
        if re.findall(r'[0-5][.]*[0-9]*',items.text):
            Ratings = items.text
        else:
            Ratings = "N/A"
    fp.write(Model.replace(",", " ") + "," + Price.replace(",", " ") + "," + Ratings + "\n")
fp.close()