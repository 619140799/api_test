# encoding: utf-8
'''
Created on 2019年1月23日

@author: QINGYUAN
'''
#导入oracle数据库操作类
from day2.cxOracleConnent import Ora  

 
class PPTDataBase():
    def GetValues(self,sql):
        #调用数据库连接工具类实现数据库连接
        db_info = {
        'dbtype':'oracle',
        'user':'system',
        'pwd':'Xin@177188',
        'host':'localhost',
        'port':'1521',
        'sid':'orcl'
        } 
        ora = Ora(db_info=db_info)
        #ora.connenct()
        #sql = "select '深交所上市公司数量' as title,count(1) as amount from gplist where substr(symbol,0,2) = 'SZ' UNION ALL select '沪交所上市公司数量' as title,count(1) as amount from gplist where substr(symbol,0,2) = 'SH'"
        rows = ora.query(sql)
        return rows
        



sql = "select leve,levenum,leveratio from leveratiotb"
pdb = PPTDataBase()
rs = pdb.GetValues(sql)
print(rs[0]['leve'])
print(rs)