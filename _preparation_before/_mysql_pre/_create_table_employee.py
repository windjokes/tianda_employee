# -*- coding: utf-8 -*-


'''
初始化创建employee工作表
'''


import pymysql

#这个def创建table的时候可以用，创建元素的时候就是坑啊！！！恶心了我一个钟头！！！
# def db_con():
#     db = pymysql.connect(
#          host='120.77.44.91',
#          user='root',
#          passwd='Chenfeng123',
#          db='tianda_i'
    #)
    # db.set_charset('utf8')
    # dbc = db.cursor()
    # dbc.execute('SET NAMES utf8;')
    # dbc.execute('SET CHARACTER SET utf8;')
    # dbc.execute('SET character_set_connection=utf8;')
    #return db

#cursor = db_con().cursor()

#创建一个table
# db = pymysql.connect(
#          host='120.77.44.91',
#          user='root',
#          passwd='Chenfeng123',
#          db='tianda_i'
#     )
#
# cursor = db.cursor()
#
# sql = "create table if not exists employee" \
#       "(" \
#       "Name varchar(60) NOT NULL, " \
#       "Count varchar(20) primary key NOT NULL, " \
#       "Id varchar(100), " \
#       "InTime datetime , " \
#       "OutTime datetime NULL, " \
#       "BasicWeeklySalary int, " \
#       "Basic4WeeksSalary int" \
# ");"
#
# cursor.execute(sql)
#
# db.close()


#插入一个模拟员工
#charset要他妈设定一下
db = pymysql.connect(
     host='120.77.44.91',
     user='root',
     passwd='Chenfeng123',
     db='tianda_i',
     charset='utf8'
    )

cursor = db.cursor()

sql = "insert into employee(Name, Count, Id, InTime, BasicWeeklySalary, Basic4WeeksSalary)" \
      "values('卢lu', '800803', '32da888888888888xx', '2017,3,20', 350, 2000)"

cursor.execute(sql)
db.commit()

db.close()