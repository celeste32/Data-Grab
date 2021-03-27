'''
EZprice示範程式-1(CSV版)
'''
import requests
from bs4 import BeautifulSoup
import csv    

searcH=input("請輸入要比價的商品名稱: ")
rQ=requests.get("https://ezprice.com.tw/s/"+searcH).text    #根據輸入的商品名稱進行搜尋
souP=BeautifulSoup(rQ,"html5lib")

            #可以使用兩個串列來模仿[表格]的資料形式
tablE=[]    #建立第一個串列用來扮演[表格(table)]的角色
for mySoup in souP.find_all("div","search-rst clearfix"):
    roW=[]     #建立此串列用來扮演[row(列)]的角色
    roW.append(mySoup.h2.a.text.strip())    #將第一欄(column)的資料加入列(row)內
    roW.append(mySoup.find("span","num").text.strip())  #將第二欄(column)的資料加入列(row)內
    roW.append(mySoup.find("span","platform-name").text.strip())    #將第三欄(column)的資料加入列(row)內
    roW.append(mySoup.h2.a["href"])     #將第四欄(column)的資料加入列(row)內
    tablE.append(roW)  #將第n列(row)的資料寫入表格(table)內
#    print(itemS)


with open(searcH+".csv","w",encoding="utf-8-sig",newline="") as csvFile:   #要讓EXCEL能順利開啟編碼得使用[utf-8-sig]
    myFile=csv.writer(csvFile)
    myFile.writerow(("品名","價格","商家","連結網址"))
    for roW in tablE:   #從模仿表格[tablE]內將資料一列列取出
        try:
            myFile.writerow((column for column in roW)) #一欄一欄地將資料寫入
        except:
            continue

with open(searcH+".csv","r",encoding="utf-8-sig") as csvFile:
    dicT=csv.DictReader(csvFile)  #將檔案內的資料以字典的形式讀入[dicT]
    for rowD in dicT:   #從字典內將資料一項項地取出
        print("商品名稱: ",rowD["品名"])
        print("價    格: ",rowD["價格"])
        print("廠商名稱: ",rowD["商家"])
        print("連結網址: ",rowD["連結網址"])
        print("------------------------------")
        #請思考一下使用字典的方式來讀取資訊有何好處???





    