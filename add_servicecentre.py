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


heading=Label(t,text='Add Service Centre', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    centreIdEntry.delete(0,100)
    cnameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    regnoEntry.delete(0,100)

    
def addcentre():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = centreIdEntry.get()
    xb = cnameEntry.get()
    xc = addressEntry.get()
    xd = phoneEntry.get()
    xe = emailEntry.get()
    xf = regnoEntry.get()

    
    sql = "insert into servicecentre values('%s','%s', '%s', '%s','%s', '%s')" %(xa,xb,xc,xd,xe,xf)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Centre Added')
    
    centreIdEntry.delete(0,100)
    cnameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    regnoEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = centreIdEntry.get()
    
    sql = "select count(*) from servicecentre where centreid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] == 0:
        messagebox.showinfo('Hi','Product not registered.')
    else:
        messagebox.showinfo('Hi', 'Product already registered!')
        
    db.close()
    

centreId=Label(t,text='Centre ID : ')
centreId.place(x=30,y=80)
centreIdEntry=Entry(t,width=20)
centreIdEntry.place(x=120,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

cname=Label(t,text='Centre Name : ')
cname.place(x=30,y=110)
cnameEntry=Entry(t,width=20)
cnameEntry.place(x=120,y=110)

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


regno=Label(t,text='Registration No. : ')
regno.place(x=30,y=230)
regnoEntry=Entry(t,width=20)
regnoEntry.place(x=120,y=230)

save=Button(t,text='Save',command=addcentre)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()