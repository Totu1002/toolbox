# -*- coding: utf-8 -*-
# url
import requests 
# html perse
from bs4 import BeautifulSoup 
#folder name⇒day_time
import datetime 
#make dir
import os
#time.sleep
import time
#path error
from urllib.parse import urljoin


#Test URL
#URL = ""

URL = input("INPUT URL : ")
#UserAgent:FireFox
header = {"User-Agent" : "Mozilla/5.0"}
#img list
images = []

def download_img(URL):
    #URL perser
    soup = BeautifulSoup(requests.get(URL,headers=header).content,'html') 
    for link in soup.find_all("img"):
        src = urljoin(URL,link.get("src")) #←←←fix error code
        if "jpg" in src:
            images.append(src)
        elif "png" in src:
            images.append(src)
        elif "gif" in src:
            images.append(src)


def main():
        #リストに値がないときメッセージ出力
        if len(images) == 0:
	        print("Warning !! Error code !!","[images] has no data")
        else:
	        #make folder
            path = "img退避フォルダ/"
            now = datetime.datetime.now()
            dirname = "img_" + now.strftime("%Y%m%d_%H%M%S")
            os.makedirs(os.path.join(path,dirname))

        for link in images:
            re = requests.get(link) 
            print("Download:",link)
            with open(os.path.join(path,dirname,link.split("/")[-1]),"wb") as f: 
                f.write(re.content) 
            time.sleep(1)

download_img(URL)
main()

print("****************************")
print("Data acquisition complete!!")
print("****************************")
