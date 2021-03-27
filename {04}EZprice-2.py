'''
EZprice示範程式-2(SQLite版)
'''
import requests
from bs4 import BeautifulSoup
import sqlite3    #載入[sqlite]第三版的模組

searcH=input("請輸入要比價的商品名稱: ")

conN=sqlite3.connect(searcH+".db") #資料庫的檔名命名為[商品名稱.db]
try:
    conN.execute("CREATE TABLE product(id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, shop TEXT, link TEXT)")    #建立一個名為[prices]的表格用來儲存資料，並且設定五個欄位，及其資料型態
    conN.commit()   #此指令的作用是把存在虛擬記憶體內的資料強迫寫入實體記憶體，因此只要牽涉到資料的異動都必須隨後使用此指令
except:
    print("資料表已經存在!!!")
    
pageS=5     #當資料的頁數很多時，設定查詢的上限頁數
for pagE in range(1,pageS):     #使用[for]迴圈一頁頁找尋資料
    rQ=requests.get("https://ezprice.com.tw/s/"+searcH+"?p="+str(pagE)).text   #根據頁數來爬取資料
    souP=BeautifulSoup(rQ,"html5lib")
    print("==================================================")
    for mySoup in souP.find_all("div","search-rst clearfix"):
        roW=[]  #建立這個串列用來暫存等一下要寫入資料庫的[列(row)/記錄(record)]
        roW.append(mySoup.h2.a.text.strip())
        roW.append(mySoup.find("span","num").text.strip())
        roW.append(mySoup.find("span","platform-name").text.strip())
        roW.append(mySoup.h2.a["href"])
        print(roW[0])
        conN.execute("INSERT INTO product(item, price, shop, link) VALUES (?,?,?,?)",roW)    #寫入一筆記錄(列)
        conN.commit()


conN.close()    #程式結束前記得把資料庫關掉






    