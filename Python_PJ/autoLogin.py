import sys
import os
import time
import signal
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def AutoLogin():

    #ブラウザアクセス
    browser.get(url)

    """
    アクセス集中時のページにリダイレクトされると
    element取得できずエラーになる
    """

    #html element 指定(対象に応じて要変更)
    login_id = browser.find_element_by_name("<element name>")
    login_pass = browser.find_element_by_name("<element name>")

    userid = "<login id>" 
    userpass = "<login pass>"

    login_id.send_keys(userid) 
    login_pass.send_keys(userpass)

    login_btn = browser.find_element_by_class_name("<class name>")
    
    login_btn.click()

#リトライカウントダウン
def count():
    max_time = 12
    for i in range(max_time):
        sec = 1
        time.sleep(sec)
        print(max_time - i)

while True:
    #URLを指定
    url = "http://**.**.**.**"

    #web driver 格納pathを指定
    chrome_driver = "/<path>/<driver name>"
    
    #option設定
    #proxy
    option = Options()
    proxy = "<proxy ip>:<proxy port>"
    option.add_argument("--proxy-server=http://%s" % proxy)

    #UserAgent
    option.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")

    #オブジェクト作成
    #browser = webdriver.Chrome(chrome_driver)
    browser = webdriver.Chrome(chrome_driver,chrome_options=option)
    browser.set_window_size(1000,550)

    try:
        res = requests.get(url,timeout=(3.0, 5.0))
        res_stat = (res.status_code == requests.codes.ok)
        if res_stat == True:
            print("--- Access completed ---")
            AutoLogin()
            break
    except:
        print("--- Time Out Error ---")
        print("--- Retry after 15 seconds  ---")
        time.sleep(3)
        #browser.close()
        browser.quit()
        os.kill(browser.service.process.pid,signal.SIGTERM)
        count()
