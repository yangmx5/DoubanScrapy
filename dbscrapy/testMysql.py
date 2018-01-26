#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","pythondb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')
# 使用execute方法执行SQL语句
cursor.execute("SELECT * from zufang")


# 使用 fetchone() 方法获取一条数据库。
#data = cursor.fetchone()
data = cursor.fetchall()


for row in data:
    title = row[0].decode('utf-8')
    link = row[1]
    time = row[2]
    count = row[3]
    print "title=%s, link=%s, time=%s, count=%s" %(title, link,time,count)

#print "Database version : %s " % data

# 关闭数据库连接
db.close()