#coding=utf-8

'''
Created on 2019年1月19日

@author: QINGYUAN
连接oracle数据库并执行语句返回结果集
'''
import cx_Oracle


class cxOracle:
    '''
    tns的取值tnsnames.ora对应的配置项的值，如：
    tns = '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.16.18.12)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=MYDB)))'
    '''
    def __init__(self,uname,upwd,tns):
        self._uname = uname
        self._upwd = upwd
        self._tns = tns
        self._conn = None
        self._Reconnect()
    def _Reconnect(self):
        if not self._conn:
            self._conn.close()
            self._conn = None
    def _NewCursor(self):
        cur = self._conn.cursor()
        if cur:
            return  cur
        else:
            print('#Error# Get New Cursor Failed.')
            return None
    def _DelCursor(self,cur):
        if cur:
            cur.close()
    #检查是否允许执行的sql语句
    def _PermitedUpdateSql(self,sql):
        rt = True
        lrsql = sql.lower()
        sql_elems = [lrsql.strip().split()]
        #update和delete最少有四个单词项
        if len(sql_elems) < 4:
            rt = False
        #更新删除语句，判断首单词，不带where语句的sql不予执行
        elif sql_elems[0] in ['update','delete']:
            if 'where' not in sql_elems:
                rt = False
        return rt
    #导出结果为文件
    def Export(self,sql,file_name,colfg='||'):
        rt = self.Query(sql)
        if rt:
            with open(file_name,'a') as fd:
                for row in rt:
                    ln_info = ''
                    for col in row:
                        ln_info += str(col) + colfg
                    ln_info += '\n'
                    fd.write(ln_info)
                    
    #查询
    def Query(self,sql,nStat=0,nNum=-1):
        rt = []
        #获取cursor
        cur = self._NewCursor()
        if not cur:
            return rt
        #查询到列表
        cur.execute(sql)
        if (nStat == 0) and (nNum == 1):
            rt.append(cur.fetchone())
        else:
            rs = cur.fetchall()
            if nNum == -1:
                rt.extend(rs[nStat:])
            else:
                rt.extend(rs[nStat:nStat + nNum])
        #释放cursor
        self._DelCursor(cur)
        return rt
    #更新
    def Exce(self,sql):
        #获取cursor
        rt = None
        cur = self._NewCursor()
        if not cur:
            return  rt 
        
        #判断Sql是否允许其执行
        if not self._PermitedUpdateSql(sql):
            return rt
        #执行语句
        rt = cur.execute(sql)
        #释放cursor
        self._DelCursor(cur)
        
#类使用示例
tns = '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=orcl)))'

ora = cxOracle('system','Xin@177188',tns)

#导出结果为文件
rs = ora.Exce('select * from a','1.txt')

#查询结果到列表
rs  = ora.Query('select * from b')
print(rs)

            
        