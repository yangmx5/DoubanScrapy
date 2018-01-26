#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

class sqlUtil():

    def __init__(self):
        try:
            # 打开数据库连接
            self.db = MySQLdb.connect("localhost","root","root","pythondb")
            # 使用cursor()方法获取操作游标
            self.cursor = self.db.cursor()
            #解决打印结果中文乱码问题
            self.cursor.execute('SET NAMES UTF8')
        except Exception as err:
            print("database erro %s" %err)


    # 使用execute方法执行SQL语句
    def queryBySql(self,str):
        sql = "SELECT * from zufang"
        self.cursor.execute(str)
        # 使用 fetchone() 方法获取一条数据库。
        #data = cursor.fetchone()
        data = self.cursor.fetchall()
        return  data

    def dealWithLinkList(self,data):
        result = []
        for row in data:
            result.append({'id':row[0],'link':row[1]})
            # result.append(row[0])
        return result

    def dataToPrint(self,data):
        for row in data:
            title = row[0].decode('utf-8')
            link = row[1]
            time = row[2]
            count = row[3]
            print "title=%s, link=%s, time=%s, count=%s" %(title, link,time,count)

    #print "Database version : %s " % data

    # 关闭数据库连接
    def closeConnection(self):
        self.db.close()


'''测试用

util = sqlUtil()
data = list(util.queryBySql("SELECT id ,link from zufang"))
# sql = "insert into zf_contents(linkid,fromuser,detailtime,userlink,contents,pic) values(12,'hello','201801-91-123 123','http://qerqc.com/asdf ','{<>}','<link>')"
sql = "insert into zf_contents(linkid,fromuser,detailtime,userlink,contents,pic) values(12,'hello','201801-91-123 123','http://qerqc.com/asdf ','{<>}','<link>')"
try:
    util.cursor.execute(sql)
    util.db.commit()
except Exception as e:
    print(e)

# temp = util.dealWithLinkList(data)
# util.dataToPrint(data)

'''