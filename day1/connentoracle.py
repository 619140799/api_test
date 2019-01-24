#coding=utf-8
import os

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

import cx_Oracle
conn_str = 'system/Xin@177188@localhost:1521/orcl'
#连接oracle数据库
conn = cx_Oracle.connect('system','Xin@177188','localhost:1521/orcl')
#connect_oracle = cx_Oracle.Connection(conn_str)
#创建cursor
cursor_oracle = conn.cursor()
#拼接sql语句
sql = 'select 10 from dual'
cursor_oracle.execute(sql)  #执行sql语句
#一次返回所有结果集fetchall
data = cursor_oracle.fetchall()
print("print all:(%s)" %data)
print("ok")
for x in data:
    print(x)
    
cursor_oracle.close()
#conn.close()



#查询include:select 
def sqlSelect(sql,db):
    cr = db.cursor()
    cr.execute(sql)
    rs = cr.fetchall()
    for i in rs:
        print(i)
    cr.close()
    return rs

#插入，更新，删除操作后需要提交include:insert,update,delete
def sqlDMl(sql,db):
    cr = db.cursor()
    cr.execute(sql)
    cr.close()
    db.commit()
    
#execute dml winth parameters
def sqlDML2(sql,params,db):
    cr = db.cursor()
    cr.execute(sql,params)
    cr.close()
    db.commit() 


sql = 'select * from course'

datatm = sqlSelect(sql, conn)

for i in datatm:
    print(i)