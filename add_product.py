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


heading=Label(t,text='Add Product', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    productIdEntry.delete(0,100)
    pnameEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    warrantyEntry.delete(0,100)

    
def addproduct():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productIdEntry.get()
    xb = pnameEntry.get()
    xc = prodTyIdEntry.get()
    xd = warrantyEntry.get()

    
    sql = "insert into product values('%s','%s', '%s', '%s')" %(xa,xb,xc,xd)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Product Added')
    
    productIdEntry.delete(0,100)
    pnameEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    warrantyEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productIdEntry.get()
    
    sql = "select count(*) from product where productid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] ==0:
        messagebox.showinfo('Hi','Product not registered.')
    else:
        messagebox.showinfo('Hi', 'Product already registered!')
        
    db.close()
    

productId=Label(t,text='Product ID : ')
productId.place(x=30,y=80)
productIdEntry=Entry(t,width=20)
productIdEntry.place(x=120,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

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
save=Button(t,text='Save',command=addproduct)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()