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


heading=Label(t,text='Find Engineer', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    engineeeridCb.delete(0,100)
    engineernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    producttypeidEntry.delete(0,100)

    
def findengineer():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = engineeeridCb.get()
    
    sql = "select ename,address,phone,email,producttypeid from engineer where engid ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    engineernameEntry.insert(0,data[0])
    addressEntry.insert(0,data[1])
    phoneEntry.insert(0,data[2])
    emailEntry.insert(0,data[3])
    producttypeidEntry.insert(0,data[4])
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select engid from engineer"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
def deleteengineer():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = engineeeridCb.get()
        
    sql = "delete from engineer where engid ='%s'" %(xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Engineer Deleted')
  
    engineeeridCb.delete(0,100)
    engineernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    producttypeidEntry.delete(0,100)
   
    
    db.close()
    
    

engineeerid=Label(t,text='Engineer ID : ')
engineeerid.place(x=30,y=80)
engineeeridCb=ttk.Combobox(t,width=20)
engineeeridCb.place(x=120,y=80)
fillcb()
engineeeridCb['values']=lt



find=Button(t,text='Find',command=findengineer)
find.place(x=280,y=80)

engineername=Label(t,text='Engineer Name : ')
engineername.place(x=30,y=110)
engineernameEntry=Entry(t,width=20)
engineernameEntry.place(x=120,y=110)

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

producttypeid=Label(t,text='Product Type ID : ')
producttypeid.place(x=30,y=230)
producttypeidEntry=Entry(t,width=20)
producttypeidEntry.place(x=120,y=230)

delete=Button(t,text='Delete',command=deleteengineer)
delete.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)



t.mainloop()