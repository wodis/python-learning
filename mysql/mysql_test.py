# encoding: utf-8
__author__ = 'wudi'

import MySQLdb

# 建立连接
connection = MySQLdb.connect("172.16.2.130", "wrm_dev", "PiZFB2ZED8cRnxRB5h1O", "wrm_dev")
# 获得cursor
cursor = connection.cursor()
# 创建sql
sql = "SELECT VERSION()"

data = None
try:
    #执行
    cursor.execute(sql)
    #解析
    data = cursor.fetchall()
except:
    print "error"

for row in data:
    print row[0]

connection.close()
