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


heading=Label(t,text='Add - Call Closing', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    engidEntry.delete(0,100)
    billEntry.delete(0,100)
    dateofcloseEntry.delete(0,100)
  
    
def addcallclosing():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    xb = callidEntry.get()
    xc = engidEntry.get()
    xd = int(billEntry.get())
    xe = dateofcloseEntry.get()
   

    
    sql = "insert into callclosing values('%s','%s', '%s',  %d, '%s')" %(xa,xb,xc,xd,xe)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Call Closing Added')
    
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    engidEntry.delete(0,100)
    billEntry.delete(0,100)
    dateofcloseEntry.delete(0,100)

    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    
    sql = "select count(*) from callclosing where callno = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] == 0:
        messagebox.showinfo('Hi','Call closing not registered.')
    else:
        messagebox.showinfo('Hi', 'Call closing already registered!')
        
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

engid=Label(t,text='Engineer ID : ')
engid.place(x=30,y=140)
engidEntry=Entry(t,width=20)
engidEntry.place(x=120,y=140)

bill=Label(t,text='Bill : ')
bill.place(x=30,y=170)
billEntry=Entry(t,width=20)
billEntry.place(x=120,y=170)

dateofclose=Label(t,text='Date of Close : ')
dateofclose.place(x=30,y=200)
dateofcloseEntry=Entry(t,width=20)
dateofcloseEntry.place(x=120,y=200)



save=Button(t,text='Save',command=addcallclosing)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()