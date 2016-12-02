from datetime import datetime
from time import time
import io, json, os, sys
import MySQLdb as mysql

########################################
#######first time to create table#######
# create table search (
# employees_id int(11) not null,
# text LONGTEXT,
# primary key (employees_id)
# )

########################################
#######table with #######
# create table search (
# employees_id int(11) not null,
# text LONGTEXT,
# primary key (employees_id)
# )



def get_db_connection():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='information_schema', charset='utf8')

def northwind():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='northwind', charset='utf8')


def generateLine():
    db = northwind()
    cursor = db.cursor()
    select = 'select * from employees where id = 1'
    cursor.execute(select)
    rows = cursor.fetchall()
    print 'len(employees) = %s' % len(rows)
    dic = ""
    for row in rows:
    	dic = row[1:]
    select = 'select * from employees e inner join orders o on e.id = o.employee_id where o.employee_id = 1 and o.id = 41'
    cursor.execute(select)
    rows = cursor.fetchall()
    dic = ""
    for row in rows:
    	dic = row[1:]
    	print dic

    db.close()
generateLine()
