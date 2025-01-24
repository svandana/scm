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


heading=Label(t,text='Show All Call Closing', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()

def showall():
    db = pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    sql = "select * from callclosing"
    msg = ''
    cur.execute(sql)
    data = cur.fetchall()
    for res in data:
        msg = msg + "\t" + res[0]
        msg = msg + "\t" + res[1]
        msg = msg + "\t" + res[2] 
        msg = msg + "\t" + str(res[3])
        msg = msg + "\t" + res[4]
        msg = msg + "\n"
        
    ta.insert(END,msg)  
    db.close()

        
ta=Text(t,width=80,height=25)
ta.place(x=30,y=80)
showall()

close=Button(t,text='Close', command=close)
close.place(x=30,y=500)




t.mainloop()