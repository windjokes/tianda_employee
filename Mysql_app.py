# -*- coding: utf-8 -*-




from peewee import *
import datetime,calendar,pymysql,arrow

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
    CheckRights = FloatField(default=2000,null=True)        #预留权益
    Fee = FloatField(default=0,null=True)                   #当期手续费
    CheckFee = FloatField(default=1800,null=True)           #预留手续费
    Cut = FloatField(default=0,null=True)                   #扣款
    Remark = CharField(default='出勤扣款：0；违规交易：0',null=True)
    CheckPay = FloatField(default=0,null=True)               #当期工资
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


#计算本周五函数，用于第一次计算，同时用于下个表格的周五计算
def this_Friday(_time):

    _thisFriday = arrow.get(_time).date()
    one_day = datetime.timedelta(days=1)

    while _thisFriday.weekday() != calendar.FRIDAY:
        _thisFriday += one_day
    return _thisFriday

#天数差的int形式
# c = this_Friday()-arrow.get().date()
# print(str(c)) #1 day, 0:00:00
# print(str(c).split(' ')[0])

#_time的下个周一
def next_Monday(_time):

    _nextMonday = arrow.get(_time).date()
    one_day = datetime.timedelta(days=1)

    while _nextMonday.weekday() != calendar.MONDAY:
        _nextMonday += one_day
    return _nextMonday



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







#QT时间强行转化为字符
def ChangeQttime2str(Q_date):
    Q_time = str(Q_date)[19:-1].replace(' ','').split(',')
    _Month = Q_time[1]
    _Day = Q_time[2]

    if int(_Month) < 10:
        _Month = '0%s'%_Month

    if int(_Day) < 10:
        _Day = '0%s'%_Day

    Q_time = "%s,%s,%s"%(Q_time[0],_Month,_Day)

    return Q_time

