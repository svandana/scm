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


heading=Label(t,text='Find - Registered Call', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberCb.delete(0,100)
    callidEntry.delete(0,100)
    productidEntry.delete(0,100)
    serviceidEntry.delete(0,100)
    docallEntry.delete(0,100)
    solvedateEntry.delete(0,100)

    
def findcallregister():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberCb.get()
    
    
    sql = "select callid,productid, serviceid, dateofcall, solvedate from callregister where callno ='%s'" %(xa) 
    
    cur.execute(sql)
    data=cur.fetchone()  
     
    callidEntry.insert(0,data[0])
    productidEntry.insert(0,data[1])
    serviceidEntry.insert(0,data[2])
    docallEntry.insert(0,data[3])
    solvedateEntry.insert(0,data[4])
  
    db.close()
  
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select callno from callregister"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
    

callnumber=Label(t,text='Call Number : ')
callnumber.place(x=30,y=80)
callnumberCb=ttk.Combobox(t,width=20)
callnumberCb.place(x=120,y=80)
fillcb()
callnumberCb['values']=lt



find=Button(t,text='Find',command=findcallregister)
find.place(x=280,y=80)

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

clear=Button(t,text='Clear',command=clear)
clear.place(x=30,y=260)

close=Button(t,text='Close', command=close)
close.place(x=100,y=260)




t.mainloop()