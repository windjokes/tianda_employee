# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import QtWidgets

from Ui__new_employee import Ui_Dialog

import sys
import pymysql



class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        #自动获取Count的值，作ID
        #链接db,不要忘记charset='utf8'
        db = pymysql.connect(
            host='120.77.44.91',
            user='root',
            port=3306,
            passwd='Chenfeng123',
            db='tianda_i',
            charset='utf8'
        )

        cursor=db.cursor()
        #从employee名单里自动获取最大Count值，作ID用
        sql="SELECT max(Count) FROM employee;"
        cursor.execute(sql)
        Count = int(cursor.fetchone()[0])+1# 获取表中最大的Count值，从mysql抓下来是个tuple
        self.lineEdit_2.setText(str(Count))

        db.close()



    # 老规矩，先来编辑一个退出跳出框来确认
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭提示', '编辑尚未完成，你确定要退出吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    #‘取消’按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        reply=QMessageBox.question(self, '关闭提示', '编辑尚未完成，确定要推出吗？',
                                   QMessageBox.Yes | QMessageBox.No,  QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass
            


    #‘提交’按钮
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """


        #QT时间格式转换成arrow可以识别的时间格式。我日啊。QT的时间居然没有月份和日期可以没有0的
        _time_ensure = str(self.dateEdit.dateTime()).replace(' ', '')[23:-5]
        t = _time_ensure.split(',')
        _time_ensure_1 = t[1]
        _time_ensure_2 = t[2]
        if int(_time_ensure_1)<10:
            _time_ensure_1= "0%s"%_time_ensure_1
        if int(_time_ensure_2)<10:
            _time_ensure_2 = "0%s" %_time_ensure_2

        _time_ensure="%s,%s,%s"%(t[0],_time_ensure_1,_time_ensure_2)
        print(_time_ensure,type(_time_ensure))



        #链接db,不要忘记charset='utf8'
        db = pymysql.connect(
            host='120.77.44.91',
            user='root',
            port=3306,
            passwd='Chenfeng123',
            db='tianda_i',
            charset='utf8'
        )

        cursor = db.cursor()




        #设置变量给新员工属性
        InTime = _time_ensure
        Name = self.lineEdit.text()
        Count = self.lineEdit_2.text()
        Id = self.lineEdit_3.text()
        #OutTime = 'Null'
        BasicWeeklySalary = self.lineEdit_4.text()
        Basic4WeeksSalary = self.lineEdit_5.text()


        #提交人员信息to employee,这里用&r最保险舒服
        sql = "insert into employee(" \
              "Name, Count, Id, " \
              "InTime," \
              "BasicWeeklySalary, Basic4WeeksSalary)" \
              "values(%r, %r, %r," \
              "%r," \
              "%r, %r);"%(
              Name, Count, Id,
              InTime,
              BasicWeeklySalary, Basic4WeeksSalary
              )

        #保险体见，专业一点
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            QMessageBox.information(self, '失败提醒',
                                    '创建新员工失败,请检查网络，然后联系风哥！')
            db.close()
            sys.exit(app.exec_())



        #下来为新员工创建独立的table
        #为新员工每个变量赋值,先暂时赋予这些值，在后面employee主程序中，某些标注的值以后要变量解决
        #给timerange作个判断
        #求本周五函数
        import datetime,calendar
        _thisFriday = datetime.date.today()
        one_day = datetime.timedelta(days=1)
        while _thisFriday.weekday() != calendar.FRIDAY:
            _thisFriday += one_day
        #这里的_thisFriday就是本周五的日期
        _thisFriday = str(_thisFriday)
        # !!!这里的函数不要丢掉，以后还会用到。
        start_time = _time_ensure    #新员工最新入职时
        #
        cycle = 0       #from 0-x,0为训练周，后面从1开始
        Count = Count
        name = Name
        #给weekly作个判断
        import arrow
        d=arrow.get(_time_ensure).weekday()
        weekly = 350-d*70#这里要作一个判断，本周的礼拜几
        print (weekly)
        #
        four_weekly = 0  #4周薪判断比较复杂
        profit = 0       #这里先给个0,留存盈利奖
        rights = 0       #动态权益
        days = 1         #周出勤
        fee = 0          #手续费
        cut =0           #扣除
        remark = ""      #备注
        real_pay =0      #实发工资
        states =0        #1-4周中的哪一周,第0周为训练周
        nature =0        #准备给1/2/3三种属性，三个class，分别给.0为训练周



        #Count作为表格名的sql
        ###槽啊，成功了！表名只能用%s,并且不能是纯数字
        sql="CREATE TABLE ks%s" \
            "(" \
            "start_time    varchar(60)," \
            "_thisFriday   date," \
            "cycle         INT(11)," \
            "Count         INT(11)," \
            "name          varchar(10) NOT NULL," \
            "weekly        INT(11)," \
            "four_weekly   INT(11)," \
            "profit        INT(11)," \
            "rights        INT(11)," \
            "days          INT(11)," \
            "fee           INT(11)," \
            "cut           INT(11)," \
            "remark        varchar(200)," \
            "real_pay      INT(11)," \
            "states        varchar(15)," \
            "nature        INT(11)" \
            ")"%str(Count)

        try:
            cursor.execute(sql)
            db.commit()
            QMessageBox.information(self, '提交成功', '新员工录入成功！')
        except:
            db.rollback()
            QMessageBox.information(self, '失败提醒',
                                    '新员工table创建失败,请检查网络，然后联系风哥！')
            db.close()
            sys.exit(app.exec_())





        # 笨方法初始化界面，一个个清除
        # InTime = _time_ensure               #时间不用初始化
        self.lineEdit.setText('')             # 清除姓名
        self.lineEdit_2.setText('800')        # 初始化账号，即员工编号
        self.lineEdit_3.setText('')           # 初始化身份证
        # 这里再次获得新的Count值，然后填入新的格子里，为下一个新员工做准备
        sql = "SELECT max(Count) FROM employee;"
        cursor.execute(sql)
        Count = int(cursor.fetchone()[0]) + 1 # 获取表中最大的Count值，从mysql抓下来是个tuple
        self.lineEdit_2.setText(str(Count))





        db.close()









        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())

