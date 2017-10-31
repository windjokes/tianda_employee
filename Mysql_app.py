# -*- coding: utf-8 -*-




from peewee import *
import datetime,calendar,pymysql

db = MySQLDatabase(
        host='120.77.44.91',
        port=3306,
        user='root',
        passwd='Chenfeng123',
        database='tianda_i',
        charset='utf8'
     )

class BaseModle(Model):

    class Meta:
        database = db



class Employee(BaseModle):

    id=IntegerField,PrimaryKeyField(unique=True)  #账户
    Name = CharField(8)                           #姓名
    _Id = CharField(32,null=True)                 #身份证
    In_Time = DateField()                         #入职时间
    Out_Time = DateField(null=True)               #离职时间
    WeeklySalary = IntegerField(default=350)      #周薪
    FourWeeklyBonus = IntegerField(default=2000)  #四周新




class Weekly(BaseModle):

    Check_Friday = DateField()                              #结算周的周五日期
    id = IntegerField()                                     #
    Name = CharField(8)
    WeeklySalary = IntegerField(default=350,null=True)      #周薪
    # FourWeeklyBonus = IntegerField(default=2000,null=True)  #四周新
    Cycle = IntegerField(default=0,null=True)
    Rights = FloatField(default=100000,null=True)           #动态权益
    ReadyRights = FloatField(default=2000,null=True)        #预留权益
    Fee = FloatField(default=0,null=True)                   #当期手续费
    ReadyFee = FloatField(default=1800,null=True)           #预留手续费
    Cut = FloatField(default=0,null=True)                   #扣款
    Remark = CharField(default='出勤扣款：0；违规交易：0',null=True)
    RealPay = FloatField(default=0,null=True)               #当期工资
    States = IntegerField(default=0)                        #状态



#创建标
#db.create_table(Weekly)


#计算上一个周五函数，用于第一次计算，同时用于下个表格的周五计算
def last_Friday():

    _lastFriday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while _lastFriday.weekday() != calendar.FRIDAY:
        _lastFriday -= one_day
    return _lastFriday


#共有多少行
def ThisFriday_Weekly_Row_Count():

    data = Weekly.select().where(Weekly.Check_Friday)
    Row_Number = 0
    for i in data:
        Row_Number+=1

    return Row_Number



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




#计算共有多少ROW






#下面是RealPay的计算函数

