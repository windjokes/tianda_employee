# -*- coding: utf-8 -*-


'''
初始化创建employee工作表
'''


import pymysql




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
