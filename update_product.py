# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:41:40 2025

@author: hivan
"""

import tkinter
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox

t = tkinter.Tk()
t.geometry('700x700')
t.title('Service Centre Management')


heading=Label(t,text='Update Product', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    productIdCb.delete(0,100)
    pnameEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    warrantyEntry.delete(0,100)

    
def findproduct():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productIdCb.get()
    
    
    sql = "select pname,producttypeid,warrantydays from product where productid ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    pnameEntry.insert(0,data[0])
    prodTyIdEntry.insert(0,data[1])
    warrantyEntry.insert(0,data[2])
    
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select productid from product"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
def updateproduct():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productIdCb.get()
    xb = pnameEntry.get()
    xc = prodTyIdEntry.get()
    xd = warrantyEntry.get()
   
  
    
    sql = "update product set pname='%s', producttypeid='%s', warrantydays='%s' where productid ='%s'" %(xb,xc,xd,xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Product Updated')
    
    productIdCb.delete(0,100)
    pnameEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    warrantyEntry.delete(0,100)
    
    
    db.close()

productId=Label(t,text='Product ID : ')
productId.place(x=30,y=80)
productIdCb=ttk.Combobox(t,width=20)
productIdCb.place(x=120,y=80)
fillcb()
productIdCb['values']=lt



find=Button(t,text='Find',command=findproduct)
find.place(x=280,y=80)

pname=Label(t,text='Product Name : ')
pname.place(x=30,y=110)
pnameEntry=Entry(t,width=20)
pnameEntry.place(x=120,y=110)

prodTyId=Label(t,text='Product Type ID : ')
prodTyId.place(x=30,y=140)
prodTyIdEntry=Entry(t,width=20)
prodTyIdEntry.place(x=120,y=140)

warranty=Label(t,text='Warranty Period : ')
warranty.place(x=30,y=170)
warrantyEntry=Entry(t,width=20)
warrantyEntry.place(x=120,y=170)

"""
email=Label(t,text='Email : ')
email.place(x=30,y=200)
emailEntry=Entry(t,width=20)
emailEntry.place(x=120,y=200)


regno=Label(t,text='Registration No. : ')
regno.place(x=30,y=230)
regnoEntry=Entry(t,width=20)
regnoEntry.place(x=120,y=230)
"""
update=Button(t,text='Update',command=updateproduct)
update.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)




t.mainloop()