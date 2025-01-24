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


heading=Label(t,text='Find Staff', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    staffIdCb.delete(0,100)
    snameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    
    
def findstaff():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = staffIdCb.get()
    
    
    sql = "select sname,address,phone,email from staff where staffid ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    snameEntry.insert(0,data[0])
    addressEntry.insert(0,data[1])
    phoneEntry.insert(0,data[2])
    emailEntry.insert(0,data[3])
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select staffid from staff"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
    
  


staffId=Label(t,text='Staff ID : ')
staffId.place(x=30,y=80)
staffIdCb=ttk.Combobox(t,width=20)
staffIdCb.place(x=120,y=80)
fillcb()
staffIdCb['values']=lt


find=Button(t,text='Find',command=findstaff)
find.place(x=280,y=80)

sname=Label(t,text='Staff Name : ')
sname.place(x=30,y=110)
snameEntry=Entry(t,width=20)
snameEntry.place(x=120,y=110)

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





clear=Button(t,text='Clear',command=clear)
clear.place(x=30,y=260)

close=Button(t,text='Close', command=close)
close.place(x=100,y=260)




t.mainloop()