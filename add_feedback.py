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


heading=Label(t,text='Add Feedback', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    engineeridEntry.delete(0,100)
    ratingEntry.delete(0,100)

    
def addfeedback():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    xb = callidEntry.get()
    xc = engineeridEntry.get()
    xd = ratingEntry.get()

    
    sql = "insert into feedback values('%s','%s', '%s', '%s')" %(xa,xb,xc,xd)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Feedback Added')
    
    callnumberEntry.delete(0,100)
    callidEntry.delete(0,100)
    engineeridEntry.delete(0,100)
    ratingEntry.delete(0,100)
    
    db.close()
    
def check():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = callnumberEntry.get()
    
    sql = "select count(*) from feedback where callno = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    if data[0] ==0:
        messagebox.showinfo('Hi','Feedback not registered.')
    else:
        messagebox.showinfo('Hi', 'Feedback already registered!')
        
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
save=Button(t,text='Save',command=addfeedback)
save.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=80,y=260)

close=Button(t,text='Close', command=close)
close.place(x=135,y=260)




t.mainloop()