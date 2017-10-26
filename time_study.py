# *.* coding=utf-8 *.*


import pymysql

#登录db
db = pymysql.connect(
         host='120.77.44.91',
         port=3306,
         user='root',
         passwd='Chenfeng123',
         db='tianda_i',
         charset='utf8'
    )
cursor = db.cursor()

sql = "create table if not exists weekly" \
      "(" \
      "Count int primary key NOT NULL," \
      "Name varchar(60) NOT NULL," \
      "GrossPay int NOT NULL," \
      "Cut int," \
      "Remark varchar(200)," \
      "NetPay int NOT NULL" \
");"
print('right')
#try:
cursor.execute(sql)
print('win')
db.commit()
print('table compelete')

# except:
#     db.rollback()
#     print('fail to create table')

db.close()


#创建实例员工

db = pymysql.connect(
         host='120.77.44.91',
         port=3306,
         user='root',
         passwd='Chenfeng123',
         db='tianda_i',
         charset='utf8'
    )
cursor = db.cursor()

Count = 800801
Name = 'gross'
GrossPay = 350
Cut = 0
Remark =''
NetPay = 350
Checked = 'Yes'
Finished = 'Yes'


sql = "insert into employee" \
      "(" \
      "Count, Name,GrossPay," \
      "Cut,Remark," \
      "NetPay,Checked,Finished" \
      ")" \
      "values" \
      "(" \
      "%r,%r,%r,%r,%r,%r,%r,%r" \
      ");"%(Count,Name,GrossPay,
      Cut,Remark,
      NetPay,Checked,Finished)


cursor.execute(sql)
db.commit()

db.close()





