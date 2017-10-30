# *.* cong=utf-8 *.*


from peewee import *


db = MySQLDatabase(
    host='120.77.44.91',
    port=3306,
    user='root',
    passwd='Chenfeng123',
    database='tianda_i',
    charset='utf8'
     )






class Weekly(Model):
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

    class Meta:
        database = db

#db.create_table(Weekly)

# Weekly.create (
#     ThisFridayDate = '2018-2-3',                  #本周五的date
#     id = 800802,                           #
#     Name = '',
#      WeeklySalary = IntegerField(default=350),      #周薪
#     FourWeeklyBonus = IntegerField(default=2000),  #四周新
#     Cycle = IntegerField(default=0),
#     Rights = FloatField(default=100000),
#     Fee = FloatField(default=0),
#     Cut = FloatField(default=0),
#     Remark = CharField(default='扣款细则：'),
#     RealPay = FloatField(default=0)
# )

db.create_table(Weekly)
db.close()

