from Tkinter import *
from math import *
from datetime import datetime
from time import time
import io, json, os, sys
import MySQLdb as mysql

def northwind():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='northwind', charset='utf8')

def evaluate(event):
	res.configure(text = "keyword: " + str(entry.get()))
	generateLine(str(entry.get()))


def generateLine(keyword):
    db = northwind()
    cursor = db.cursor()
    select = "select tablename, id from search where text like \"%" + keyword + "%\""
    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
    	tablename = row[0]
    	id = row[1]
    	select = "select * from %s where id = %s"%(tablename, id)
    	cursor.execute(select)
    	answers = cursor.fetchall()
    	answer = answers[0]
    	print answer

    	# select = "show columns from %s"%tablename
    	# cursor.execute(select)
    	# columns = cursor.fetchall()
    	





    db.close()


w = Tk()
Label(w, text="Search").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
