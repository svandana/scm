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


heading=Label(t,text='Update Customer', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    customeridCb.delete(0,100)
    customernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    productidEntry.delete(0,100)

    
def findcustomer():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = customeridCb.get()
    
    
    sql = "select cname,address,phone,email,productid from customer where customerid ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    customernameEntry.insert(0,data[0])
    addressEntry.insert(0,data[1])
    phoneEntry.insert(0,data[2])
    emailEntry.insert(0,data[3])
    productidEntry.insert(0,data[4])
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select customerid from customer"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
def updatecustomer():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = customeridCb.get()
    xb = customernameEntry.get()
    xc = addressEntry.get()
    xd = phoneEntry.get()
    xe = emailEntry.get()
    xf = productidEntry.get()
  
    
    sql = "update customer set cname='%s', address='%s', phone='%s', email='%s',productid = '%s' where customerid ='%s'" %(xb,xc,xd,xe,xf,xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Customer Updated')
    
    customeridCb.delete(0,100)
    customernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    productidEntry.delete(0,100)
    
    
    db.close()
    
    

customerid=Label(t,text='Customer ID : ')
customerid.place(x=30,y=80)
customeridCb=ttk.Combobox(t,width=20)
customeridCb.place(x=120,y=80)
fillcb()
customeridCb['values']=lt




find=Button(t,text='Find',command=findcustomer)
find.place(x=280,y=80)

customername=Label(t,text='Customer Name : ')
customername.place(x=30,y=110)
customernameEntry=Entry(t,width=20)
customernameEntry.place(x=120,y=110)

address=Label(t,text='Address : ')
address.place(x=30,y=140)
addressEntry=Entry(t,width=20)
addressEntry.place(x=120,y=140)

phone=Label(t,text='Phone : ')
phone.place(x=30,y=170)
phoneEntry=Entry(t,width=20)
phoneEntry.place(x=120,y=170)

email=Label(t,text='Email : ')
email.place(x=30,y=200)
emailEntry=Entry(t,width=20)
emailEntry.place(x=120,y=200)

productid=Label(t,text='Product ID : ')
productid.place(x=30,y=230)
productidEntry=Entry(t,width=20)
productidEntry.place(x=120,y=230)

update=Button(t,text='Update',command=updatecustomer)
update.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)





t.mainloop()