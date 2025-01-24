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


heading=Label(t,text='Update Service Centre', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    centreIdCb.delete(0,100)
    cnameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    regnoEntry.delete(0,100)
    
def finddata():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = centreIdCb.get()
    
    sql = "select cname,address,phone,email,regno from servicecentre where centreid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    cnameEntry.insert(0,data[0])
    addressEntry.insert(0,data[1])
    phoneEntry.insert(0,data[2])
    emailEntry.insert(0,data[3])
    regnoEntry.insert(0,data[4])
    
    db.close()
    
    
    
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select centreid from servicecentre"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
    
    
def updatecentre():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = centreIdCb.get()
    xb = cnameEntry.get()
    xc = addressEntry.get()
    xd = phoneEntry.get()
    xe = emailEntry.get()
    xf = regnoEntry.get()
    
    sql = "update servicecentre set cname='%s', address='%s', phone='%s', email='%s',regno='%s' where centreid ='%s'" %(xb,xc,xd,xe,xf,xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Service Centre Updated')
    
    centreIdCb.delete(0,100)
    cnameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    regnoEntry.delete(0,100)
    
    db.close()
    


centreId=Label(t,text='Centre ID : ')
centreId.place(x=30,y=80)
centreIdCb=ttk.Combobox(t,width=20)
centreIdCb.place(x=120,y=80)
fillcb()
centreIdCb['values']=lt



find=Button(t,text='Find',command=finddata)
find.place(x=280,y=80)

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

update=Button(t,text='Update',command=updatecentre)
update.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)




t.mainloop()