import operator
import math, random, sys, csv 
import MySQLdb as mysql
from utils import parse, print_results


def connect_information():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='information_schema', charset='utf8')

def connect_northwind():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='northwind', charset='utf8')


def getTables():
    db = connect_information()
    cursor = db.cursor()
    select = 'select table_name from tables where table_schema = \"northwind\" and table_name != \"search\" and table_name != \"employee_privileges\" and table_name != \"strings\" and table_name != \"sales_reports\";'
    cursor.execute(select)
    tables = cursor.fetchall()
    for table in tables:
        print table
        select = "select COLUMN_NAME from key_column_usage where CONSTRAINT_SCHEMA = \"northwind\" and constraint_name = \"primary\" and table_name = \"%s\";"%table
        cursor.execute(select)
        lines = cursor.fetchall()
        for line in lines:
            generate_sql(table[0], "new.sql", line[0])



    db.close()


# select * from key_column_usage where CONSTRAINT_SCHEMA = "northwind" and constraint_name = "primary" and table_name != "search";
# 




def generate_sql(tableName, fnOut, primaryKey):
    db = connect_northwind()
    cursor = db.cursor()
    select = 'select %s from %s'%(primaryKey, tableName)

    cursor.execute(select)
    keys = cursor.fetchall()

    f = open(fnOut, 'a')

    for key in keys:
        id = key[0]
        select = 'select * from %s where %s = %s'%(tableName, primaryKey, id)

        print select
        cursor.execute(select)
        x = cursor.fetchall()
        x = x[0]
        

        text = ""

        for item in x:
            try:
                item = item.encode("utf-8")
            except:
                pass

            text = text + " " + str(item)
        select = 'select rank from %s where %s = %s'%(tableName, primaryKey, id)
        cursor.execute(select)
        x = cursor.fetchall()
        x = x[0][0]
        if (x == None):
            x = 0
        

        line = "insert into search values (%s, \"%s\", \"%s\", %s);\n"%(key[0], tableName, text.decode("utf-8"), x)
        f.write(line.encode("utf-8"))
    db.close()
getTables()

