# -*- coding: utf-8 -*-




from peewee import *
import datetime,calendar,pymysql



class BaseModle(Model):

    class Meta:

        database = MySQLDatabase(
            host='120.77.44.91',
            port=3306,
            user='root',
            passwd='Chenfeng123',
            database='tianda_i',
            charset='utf8'
             )

class Employee(BaseModle):

    id=IntegerField,PrimaryKeyField(unique=True)  #账户
    Name = CharField(8)                           #姓名
    _Id = CharField(32,null=True)                 #身份证
    In_Time = DateField()                         #入职时间
    Out_Time = DateField(null=True)               #离职时间
    WeeklySalary = IntegerField(default=350)      #周薪
    FourWeeklyBonus = IntegerField(default=2000)  #四周新




class Weekly(BaseModle):

    ThisFridayDate = DateField()                  #本周五的date
    id = IntegerField()                           #
    Name = CharField(8)
    WeeklySalary = IntegerField(default=350,null=True)      #周薪
    FourWeeklyBonus = IntegerField(default=2000,null=True)  #四周新
    Cycle = IntegerField(default=0,null=True)
    Rights = FloatField(default=100000,null=True)
    Fee = FloatField(default=0,null=True)
    Cut = FloatField(default=0,null=True)
    Remark = CharField(default='扣款细则：',null=True)
    RealPay = FloatField(default=0,null=True)



#计算上一个周五函数
def last_Friday():

    _lastFriday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while _lastFriday.weekday() != calendar.FRIDAY:
        _lastFriday -= one_day
    return _lastFriday


#计算最大id
def max_id():

    db = pymysql.connect(
        host='120.77.44.91',
        user='root',
        port=3306,
        passwd='Chenfeng123',
        db='tianda_i',
        charset='utf8'
    )

    cursor=db.cursor()
        #从employee名单里自动获取最大id值，作ID用
    sql="SELECT max(id) FROM employee;"
    cursor.execute(sql)
    id = int(cursor.fetchone()[0])+1# 获取表中最大的id值，从mysql抓下来是个tuple
    db.close()

    return id

