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


heading=Label(t,text='Add Product Type', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    productTyIdEntry.delete(0,100)
    typenameEntry.delete(0,100)
    descriptionEntry.delete(0,100)
    

    
def addproducttype():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productTyIdEntry.get()
    xb = typenameEntry.get()
    xc = descriptionEntry.get()
    
    sql = "insert into producttype values('%s','%s', '%s')" %(xa,xb,xc)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Product Type Added')
    
    productTyIdEntry.delete(0,100)
    typenameEntry.delete(0,100)
    descriptionEntry.delete(0,100)
        
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productTyIdEntry.get()
    
    sql = "select count(*) from producttype where producttypeid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] ==0:
        messagebox.showinfo('Hi','Product Type Not Registered.')
    else:
        messagebox.showinfo('Hi', 'Product Type Already Registered!')
        
    db.close()
    

productTyId=Label(t,text='Product Type ID : ')
productTyId.place(x=30,y=80)
productTyIdEntry=Entry(t,width=20)
productTyIdEntry.place(x=145,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

typename=Label(t,text='Product Type Name : ')
typename.place(x=30,y=110)
typenameEntry=Entry(t,width=20)
typenameEntry.place(x=145,y=110)

description=Label(t,text='Product Description : ')
description.place(x=30,y=140)
descriptionEntry=Entry(t,width=20)
descriptionEntry.place(x=145,y=140)

"""
warranty=Label(t,text='Warranty Period : ')
warranty.place(x=30,y=170)
warrantyEntry=Entry(t,width=20)
warrantyEntry.place(x=120,y=170)

email=Label(t,text='Email : ')
email.place(x=30,y=200)
emailEntry=Entry(t,width=20)
emailEntry.place(x=120,y=200)


regno=Label(t,text='Registration No. : ')
regno.place(x=30,y=230)
regnoEntry=Entry(t,width=20)
regnoEntry.place(x=120,y=230)
"""
save=Button(t,text='Save',command=addproducttype)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()