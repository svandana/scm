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


heading=Label(t,text='Update - Call Closing', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberCb.delete(0,100)
    callidEntry.delete(0,100)
    engidEntry.delete(0,100)
    billEntry.delete(0,100)
    dateofcloseEntry.delete(0,100)
  
    
def findcallclosing():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberCb.get()
    
    
    sql = "select callid,engid, bill, dateofclose  from callclosing where callno ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    callidEntry.insert(0,data[0])
    engidEntry.insert(0,data[1])
    billEntry.insert(0,str(data[2]))
    dateofcloseEntry.insert(0,data[3])
    
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select callno from callclosing"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
def updatecallclosing():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberCb.get()
    xb = callidEntry.get()
    xc = engidEntry.get()
    xd = int(billEntry.get())
    xe = dateofcloseEntry.get()
    
    sql = "update callclosing set callid='%s', engid='%s', bill=%d, dateofclose='%s' where callno ='%s'" %(xb,xc,xd,xe,xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Call Closing Updated')
    
    callnumberCb.delete(0,100)
    callidEntry.delete(0,100)
    engidEntry.delete(0,100)
    billEntry.delete(0,100)
    dateofcloseEntry.delete(0,100)
    
    db.close()    
    


callnumber=Label(t,text='Call Number : ')
callnumber.place(x=30,y=80)
callnumberCb=ttk.Combobox(t,width=20)
callnumberCb.place(x=120,y=80)
fillcb()
callnumberCb['values']=lt


find=Button(t,text='Find',command=findcallclosing)
find.place(x=280,y=80)

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



update=Button(t,text='Update',command=updatecallclosing)
update.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)



t.mainloop()