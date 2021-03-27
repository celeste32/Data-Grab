'''
EZprice示範程式-4(SQLite[資料呈現]版)
'''
import sqlite3  #載入[sqlite]第三版的模組

searcH=input("請輸入要查詢的資料庫名稱: ")

conN=sqlite3.connect(searcH+".db") #資料庫的檔名命名為[商品名稱.db]

tablE=conN.execute("SELECT * FROM product")    #找出表格內的所有記錄
for recorD in tablE:
    print("商品名稱: ",recorD[1])
    print("價    格: ",recorD[2])
    print("廠商名稱: ",recorD[3])
    print("連結網址: ",recorD[4])
    print("------------------------------")



conN.close()






    