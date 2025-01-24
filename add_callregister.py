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


heading=Label(t,text='Add - Register Call', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    productidEntry.delete(0,100)
    serviceidEntry.delete(0,100)
    docallEntry.delete(0,100)
    solvedateEntry.delete(0,100)

    
def addcallregister():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    xb = callidEntry.get()
    xc = productidEntry.get()
    xd = serviceidEntry.get()
    xe = docallEntry.get()
    xf = solvedateEntry.get()

    
    sql = "insert into callregister values('%s','%s', '%s', '%s', '%s', '%s')" %(xa,xb,xc,xd,xe,xf)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Call Registered')
    
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    productidEntry.delete(0,100)
    serviceidEntry.delete(0,100)
    docallEntry.delete(0,100)
    solvedateEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    
    sql = "select count(*) from callregister where callno = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] == 0:
        messagebox.showinfo('Hi','Call number not registered.')
    else:
        messagebox.showinfo('Hi', 'Call number already registered!')
        
    db.close()
    

callnumber=Label(t,text='Call Number : ')
callnumber.place(x=30,y=80)
callnumberEntry=Entry(t,width=20)
callnumberEntry.place(x=120,y=80)

check=Button(t,text='Check',command=check)
check.place(x=280,y=80)

callid=Label(t,text='Call ID : ')
callid.place(x=30,y=110)
callidEntry=Entry(t,width=20)
callidEntry.place(x=120,y=110)

productid=Label(t,text='Product ID : ')
productid.place(x=30,y=140)
productidEntry=Entry(t,width=20)
productidEntry.place(x=120,y=140)

serviceid=Label(t,text='Service ID : ')
serviceid.place(x=30,y=170)
serviceidEntry=Entry(t,width=20)
serviceidEntry.place(x=120,y=170)

docall=Label(t,text='Date of Call : ')
docall.place(x=30,y=200)
docallEntry=Entry(t,width=20)
docallEntry.place(x=120,y=200)

solvedate=Label(t,text='Solve Date : ')
solvedate.place(x=30,y=230)
solvedateEntry=Entry(t,width=20)
solvedateEntry.place(x=120,y=230)

save=Button(t,text='Save',command=addcallregister)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()