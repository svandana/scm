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


heading=Label(t,text='Find Feedback', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberCb.delete(0,100)
    callidEntry.delete(0,100)
    engineeridEntry.delete(0,100)
    ratingEntry.delete(0,100)

    
def findfeedback():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberCb.get()
  
    sql = "select callid,engid,rating from feedback where callno ='%s'" %(xa)
    
    cur.execute(sql)
    data = cur.fetchone()
    
    
    callidEntry.insert(0,data[0])
    engineeridEntry.insert(0,data[1])
    ratingEntry.insert(0,data[2])
    
    db.close()
    
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select callno from feedback"
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


find=Button(t,text='Find',command=findfeedback)
find.place(x=280,y=80)

callid=Label(t,text='Call ID : ')
callid.place(x=30,y=110)
callidEntry=Entry(t,width=20)
callidEntry.place(x=120,y=110)

engineerid=Label(t,text='Engineer ID : ')
engineerid.place(x=30,y=140)
engineeridEntry=Entry(t,width=20)
engineeridEntry.place(x=120,y=140)

rating=Label(t,text='Rating : ')
rating.place(x=30,y=170)
ratingEntry=Entry(t,width=20)
ratingEntry.place(x=120,y=170)

"""
email=Label(t,text='Email : ')
email.place(x=30,y=200)
emailEntry=Entry(t,width=20)
emailEntry.place(x=120,y=200)


regno=Label(t,text='Registration No. : ')
regno.place(x=30,y=230)
regnoEntry=Entry(t,width=20)
regnoEntry.place(x=120,y=230)
"""
clear=Button(t,text='Clear',command=clear)
clear.place(x=30,y=260)

close=Button(t,text='Close', command=close)
close.place(x=100,y=260)




t.mainloop()