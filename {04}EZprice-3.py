'''
EZprice示範程式-3(SQLite[記錄不重複儲存]版)
'''
import requests
from bs4 import BeautifulSoup
import sqlite3  #載入[sqlite]第三版的模組

searcH=input("請輸入要比價的商品名稱: ")

conN=sqlite3.connect(searcH+".db") #資料庫的檔名命名為[商品名稱.db]

try:
    conN.execute("CREATE TABLE product(id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, shop TEXT, link TEXT)")
    conN.commit()
except:
    print("資料表已經存在!!!")

pageS=6     #搜尋的頁數上限可自行根據需求決定
for pagE in range(1,pageS):
    rQ=requests.get("https://ezprice.com.tw/s/"+searcH+"?p="+str(pagE)).text
    souP=BeautifulSoup(rQ,"html5lib")
    for mySoup in souP.find_all("div","search-rst clearfix"):
        tablE=conN.execute("SELECT * FROM product WHERE item = ?",(mySoup.h2.a.text.strip(),))    #先以此指令尋找表格內是否有相同的記錄
        exisT=tablE.fetchone() #使用[fetchone()]方法，若沒找到資料會傳回[None]
        if exisT is None:
            roW=[]  #建立這個串列用來暫存等一下要寫入資料庫的[列(row)/記錄(record)]
            roW.append(mySoup.h2.a.text.strip())
            roW.append(mySoup.find("span","num").text.strip())
            roW.append(mySoup.find("span","platform-name").text.strip())
            roW.append(mySoup.h2.a["href"])
            print(roW[0])
            conN.execute("INSERT INTO product(item, price, shop, link) VALUES (?,?,?,?)",roW)
            conN.commit()
        else:    
            print("此筆資料已經存在!!!")


conN.close()






    