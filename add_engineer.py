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


heading=Label(t,text='Add Engineer', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    engineeeridEntry.delete(0,100)
    engineernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    producttypeidEntry.delete(0,100)

    
def addengineer():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = engineeeridEntry.get()
    xb = engineernameEntry.get()
    xc = addressEntry.get()
    xd = phoneEntry.get()
    xe = emailEntry.get()
    xf = producttypeidEntry.get()

    
    sql = "insert into engineer values('%s','%s', '%s', '%s', '%s', '%s')" %(xa,xb,xc,xd,xe,xf)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Engineer Added')
    
    engineeeridEntry.delete(0,100)
    engineernameEntry.delete(0,100)
    addressEntry.delete(0,100)
    phoneEntry.delete(0,100)
    emailEntry.delete(0,100)
    producttypeidEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = engineeeridEntry.get()
    
    sql = "select count(*) from engineer where engid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] == 0:
        messagebox.showinfo('Hi','Engineer not registered.')
    else:
        messagebox.showinfo('Hi', 'Engineer already registered!')
        
    db.close()
    

engineeerid=Label(t,text='Engineer ID : ')
engineeerid.place(x=30,y=80)
engineeeridEntry=Entry(t,width=20)
engineeeridEntry.place(x=120,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

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

save=Button(t,text='Save',command=addengineer)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()