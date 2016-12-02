from datetime import datetime
from time import time
import io, json, os, sys
import MySQLdb as mysql

def get_db_connection():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='information_schema', charset='utf8')

def northwind():
    return mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='f', db='northwind', charset='utf8')



def generate_csv(dbName, fnOut):
    db = get_db_connection()
    cursor = db.cursor()
    select = 'select TABLE_NAME,COLUMN_NAME,REFERENCED_TABLE_NAME from KEY_COLUMN_USAGE where TABLE_SCHEMA = %s and referenced_column_name IS NOT NULL'
    params = (dbName,)
    cursor.execute(select, params)
    rows = cursor.fetchall()
    print 'len(rows) = %s' % len(rows)
    constraints = {}
    for row in rows:
        print row
        table_name,column_name,referenced_table_name = row
        if table_name not in constraints:
            constraints[table_name] = {}
        constraints[table_name][column_name] = referenced_table_name
    print 'len(constraints) = %s' % len(constraints)
    print '======================================\n\n'
    db.close()




    
    db = northwind()
    cursor = db.cursor()
    with io.open(fnOut, 'w', encoding='utf-8') as f:
        for table_name in constraints:
            # get primary key
            select = 'SHOW INDEX FROM %s WHERE Key_name = "PRIMARY"' % table_name
            cursor.execute(select)
            rows = cursor.fetchall()
            primary_key = rows[0][4]
            print '%s: %s' % (table_name, primary_key)
            # generate select
            columns = set()
            columns.add(primary_key)
            columns.update(constraints[table_name].keys())
            columns = list(columns)
            select = 'SELECT %s FROM %s' % (','.join(columns), table_name)
            print select
            cursor.execute(select)
            rows = cursor.fetchall()

            for row in rows:
                print row
                pidx = columns.index(primary_key, )
                print pidx
                pval = row[pidx]
                print pval
                for col,ref in constraints[table_name].items():
                    cidx = columns.index(col, )
                    cval = row[cidx]
                    print re
                    print cval
                    f.write('%s-%s,%s,%s-%s,%s\n' % (table_name, pval, 0, ref, cval, 1))
#             break
    f.close()
    db.close()
#     with io.open(fnOut, encoding=u'utf-8') as f:
#         f.write

if __name__ == '__main__':
    print datetime.today()
    t0 = time()

    generate_csv(u'northwind', u'northwind.csv')

    print time() - t0

