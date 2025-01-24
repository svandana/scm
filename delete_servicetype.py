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


heading=Label(t,text='Delete Service Type', font=('helvetica',14))
heading.place(x=30,y=30)

def close():
    t.destroy()
    
def clear():
    serviceIdCb.delete(0,100)
    productIdEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    snameEntry.delete(0,100)
    costEntry.delete(0,100)
    daysSolveEntry.delete(0,100)
    
def finddata():
    db = pymysql.connect(host='localhost', user='root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = serviceIdCb.get()
    
    sql = "select productid,producttypeid,sname,cost,daystosolve from servicetype where serviceid = '%s'" %(xa)
    cur.execute(sql)
    data=cur.fetchone()
    
    productIdEntry.insert(0,data[0])
    prodTyIdEntry.insert(0,data[1])
    snameEntry.insert(0,data[2])
    costEntry.insert (0,str(data[3]))
    daysSolveEntry.insert(0,data[4])
    
    db.close()
    
    
    
lt=[]    
def fillcb():
    db = pymysql.connect(host='localhost', user = 'root',password = 'root',database ='scm')
    cur = db.cursor()
    
    sql = "select serviceid from servicetype"
    cur.execute(sql)
    data=cur.fetchall()
    for res in data:
        lt.append(res[0])
    db.close()    
    
    
    
def deleteservice():
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'root', database = 'scm')
    cur = db.cursor()
    
    xa = serviceIdCb.get()
    
    
    sql = "delete from servicetype where serviceid ='%s'" %(xa)
    
    cur.execute(sql)
    db.commit()
    
    messagebox.showinfo('Hi','Service Type Deleted')
    
    serviceIdCb.delete(0,100)
    productIdEntry.delete(0,100)
    prodTyIdEntry.delete(0,100)
    snameEntry.delete(0,100)
    costEntry.delete(0,100)
    daysSolveEntry.delete(0,100)
    
    db.close()
    


serviceId=Label(t,text='Service ID : ')
serviceId.place(x=30,y=80)
serviceIdCb=ttk.Combobox(t,width=20)
serviceIdCb.place(x=120,y=80)
fillcb()
serviceIdCb['values']=lt



find=Button(t,text='Find',command=finddata)
find.place(x=280,y=80)

productId=Label(t,text='Product Id : ')
productId.place(x=30,y=110)
productIdEntry=Entry(t,width=20)
productIdEntry.place(x=120,y=110)

prodTyId=Label(t,text='Product Type Id : ')
prodTyId.place(x=30,y=140)
prodTyIdEntry=Entry(t,width=20)
prodTyIdEntry.place(x=120,y=140)

sname=Label(t,text='Service Name : ')
sname.place(x=30,y=170)
snameEntry=Entry(t,width=20)
snameEntry.place(x=120,y=170)

cost=Label(t,text='Service Cost : ')
cost.place(x=30,y=200)
costEntry=Entry(t,width=20)
costEntry.place(x=120,y=200)


daysSolve=Label(t,text='Days to Solve : ')
daysSolve.place(x=30,y=230)
daysSolveEntry=Entry(t,width=20)
daysSolveEntry.place(x=120,y=230)

delete=Button(t,text='Delete',command=deleteservice)
delete.place(x=30,y=260)

clear=Button(t,text='Clear',command=clear)
clear.place(x=90,y=260)

close=Button(t,text='Close', command=close)
close.place(x=145,y=260)




t.mainloop()