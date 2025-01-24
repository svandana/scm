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


heading=Label(t,text='Add Customer', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    customeridEntry.delete(0,100)
    customernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    productidEntry.delete(0,100)

    
def addcustomer():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = customeridEntry.get()
    xb = customernameEntry.get()
    xc = addressEntry.get()
    xd = phoneEntry.get()
    xe = emailEntry.get()
    xf = productidEntry.get()

    
    sql = "insert into customer values('%s','%s', '%s', '%s', '%s', '%s')" %(xa,xb,xc,xd,xe,xf)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Customer Added')
    
    customeridEntry.delete(0,100)
    customernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    productidEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = customeridEntry.get()
    
    sql = "select count(*) from customer where customerid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] == 0:
        messagebox.showinfo('Hi','Customer not registered.')
    else:
        messagebox.showinfo('Hi', 'Customer already registered!')
        
    db.close()
    

customerid=Label(t,text='Customer ID : ')
customerid.place(x=30,y=80)
customeridEntry=Entry(t,width=20)
customeridEntry.place(x=120,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

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

save=Button(t,text='Save',command=addcustomer)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()