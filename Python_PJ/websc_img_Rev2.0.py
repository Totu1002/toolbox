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
#pass error
from urllib.parse import urljoin
#GUI
import tkinter
from tkinter import messagebox
#Subprocess
import subprocess

#tkinter for GUI
root = tkinter.Tk()
root.title(u"websc_prot_Rev1.5.py") 
root.geometry("500x300")
root.configure(bg="#000000")

#icon
#16*16で変換して任意のものを同ディレクトリへ配置
#error from icloud ?
#iconfile = "python_tk.ico" 
#root.iconbitmap(default=iconfile)
#root.iconbitmap(default="python_tk.ico")

#label
static1 = tkinter.Label(text=u"▼Enter the target URL▼",font=("",15,"bold"),bg="#000000",fg="#00FF00")
#static1.place(y=20)
static1.pack(pady=10)

#UserAgent:FireFox
header = {"User-Agent" : "Mozilla/5.0"}
#img list
images = []

def download_img(URL):
    #URL perser
    soup = BeautifulSoup(requests.get(URL,headers=header).content,'lxml') 
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
	        print("[images] has no data")
	        messagebox.showerror("Warning !! Error code !!","[images] has no data")
	        root.quit()
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
            time.sleep(3)


#Entry_box value send
def send_Botton():
    
    URL = Entry_box.get()
    download_img(URL)
    main()

    print("****************************")
    print("Data acquisition complete!!")
    print("****************************")

    messagebox.showinfo("■ Processing complete ■","Data acquisition complete!!")
    Entry_box.delete(0, tkinter.END)
    #root.quit()

#Entry_box value delete
def delete_Botton():
    Entry_box.delete(0, tkinter.END)

#Entry box
Entry_box = tkinter.Entry(width=70)
Entry_box.pack()

#Button1
#関数へ引数を渡す。
Button1 = tkinter.Button(text=u"Download",width=20,command=send_Botton)
Button1.pack(padx=50,pady=10,side = 'left')

#Button2
Button2 = tkinter.Button(text=u'Erase',width=20,command=delete_Botton)
Button2.pack(padx=50,pady=10,side = 'right')

root.mainloop()


#追記:tkinterの機能拡張を検討。19/11/05
#更新メモ：保存に関する処理を修正 19/11/12

