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


heading=Label(t,text='Update Product Type', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    productTyIdCb.delete(0,100)
    typenameEntry.delete(0,100)
    descriptionEntry.delete(0,100)

    
def findproducttype():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productTyIdCb.get()
    
    
    sql = "select typename,description from producttype where producttypeid ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    typenameEntry.insert(0,data[0])
    descriptionEntry.insert(0,data[1])
 
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select producttypeid from producttype"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close() 
    
def deleteproducttype():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = productTyIdCb.get()
        
    sql = "delete from producttype where producttypeid ='%s'" %(xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Product Type Deleted')
    
    productTyIdCb.delete(0,100)
    typenameEntry.delete(0,100)
    descriptionEntry.delete(0,100)
    
    db.close()
    

   
  
    
 

productTyId=Label(t,text='Product Type ID : ')
productTyId.place(x=30,y=80)
productTyIdCb=ttk.Combobox(t,width=20)
productTyIdCb.place(x=145,y=80)
fillcb()
productTyIdCb['values']=lt


find=Button(t,text='Find',command=findproducttype)
find.place(x=300,y=80)

typename=Label(t,text='Product Type Name : ')
typename.place(x=30,y=110)
typenameEntry=Entry(t,width=20)
typenameEntry.place(x=145,y=110)

description=Label(t,text='Product Description : ')
description.place(x=30,y=140)
descriptionEntry=Entry(t,width=20)
descriptionEntry.place(x=145,y=140)

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



delete=Button(t,text='Delete',command=deleteproducttype)
delete.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)



t.mainloop()