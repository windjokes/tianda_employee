# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot,QStringListModel
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.Qt import QString

from Ui__new_employee import Ui_Dialog

import sys
import pymysql
import datetime



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
        #QT时间格式转换
        _time_ensure = str(self.dateEdit.dateTime(), encoding='utf-8')[23:-5]
        
        print(_time_ensure)
#        _time_ensure = '%s,0'%_time_ensure
#        print(_time_ensure)
#        full_time = _time_ensure.split(',')
#        print (full_time)
#            #这里加判断，把‘0加上’--让我们互相恶心吧,苦啊！
#        if len(full_time[1]) != 2:
#            full_time[1] = '0%s'%full_time[1]
#        else:
#            pass
#        if len(full_time[2]) != 2:
#            full_time[2] = '0%s'%full_time[2]
#        else:
#            pass
#        
#        ensure_time = "%s-%s-%s"%(full_time[0],
#        full_time[1], full_time[2])
#        print(ensure_time)
        #ensure_time = datetime.datetime.strptime(ensure_time,  "%Y-%m-%d %H:%M:%S")
        #print(ensure_time)
        #设置变量给新员工属性
#        Name = self.lineEdit.text()
#        print(Name)
#        Count = self.lineEdit_2.text()
#        Id = self.lineEdit_3
#        InTime = ensure_time
#        OutTime = 'Null'
#        BasicWeeklySalary = self.lineEdit_4
#        Basic4WeeksSalary = self.lineEdit_5

        #链接db,不要忘记charset='utf8'
        db = pymysql.connect(
            host='120.77.44.91',
            user='root',
            passwd='Chenfeng123',
            db='tianda_i',
            charset='utf8'
        )

        cursor= db.cursor()

        #提交人员信息
        # sql = "insert into employee(" \
        #       "Name, Count, Id, " \
        #       "InTime, OutTime," \
        #       "BasicWeeklySalary, Basic4WeeksSalary)" \
        #       "values(%s, %s, %s," \
        #       "%s, %s," \
        #       "%d, %d)"%(Name, Count, Id, InTime, OutTime, BasicWeeklySalary, Basic4WeeksSalary)

        sql = "insert into employee(Name,Count,Intime) values('wangli', '800804', '2017, 5,20')"

        #保险体见，专业一点
        #try:
        cursor.execute(sql)
        db.commit()

        #except:
         #   db.rollback()
            #QMessageBox.information(self,'失败提醒','新员工失败,请检查网络，然后联系风哥！')
            #db.close()
            #sys.exit(app.exec_())

        db.close()









        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())

