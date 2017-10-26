# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.

db = pymysql.connect(
        '120.77.44.91',
        'root',
        'Chenfeng123'
        'tianda_i'
    )


"""



from PyQt5.QtCore import pyqtSlot, QDateTime
from PyQt5.QtWidgets import QMainWindow,  QMessageBox
from PyQt5 import QtWidgets

import pymysql
import time
import sys
#import datetime

from Ui_employee import Ui_MainWindow
from _new_employee import Dialog







class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.

    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #老子现在不来和你死磕！！！等老子做好了，再来和你磕！
        # 初始化时候尝试获取服务器时间，写入weekcount里(ps:以后可以放在登陆界面的按钮后面触发，这里只能先这样了，先出WARNING，再出界面)
        # try:
        #
        #     db = pymysql.connect(
        #         host='120.77.44.91',
        #         user='root',
        #         passwd='Chenfeng123',
        #         db='tianda_i',
        #         charset='utf8'
        #     )
        #
        #     cursor = db.cursor()
        #     cursor.execute("select date_format(now(),'%Y%m%d%H%i%s')")
        #
        #     _date = cursor.fetchall()[0][0][0:8]  # 这边获取时间成功20171021
        #
        #     print(_date)
        #     print(_date[0:4], _date[4:6], _date[6:8] )
        #
        #     _date= '%s-%s-%s'%(_date[0:4], _date[4:6], _date[6:8])
        #     print(_date)
        #     #mysql里算两个日期相减，得到天数：
        #     cursor.execute("select datediff(_date, '%s-01-01')"%_date[0:4])
        #     __days=cursor.fetchall()
        #     print(__days)
        #     db.close()
            
            
        #     _weekly_count=int(_days)/7
        #     print(_weekly_count)
        #     self.label_weekcount.setText('今天是%s\n本年度第%d周'%(_date, _weekly_count))
        #
        #
        #
        # except:

        try:
            #抓取本地时间
            _date=time.strftime("%Y-%m-%d", time.localtime())
            #算出本年度周数，本地时间就是他妈简单
            _weekly_count = time.strftime("%W")
            #print(_weekly_count)
                #写入本地时间
            self.label_weekcount.setText('今天是%s\n本年度第%d周'%(_date,int(_weekly_count)))
            

        except:
            QMessageBox.warning(self,'抓取本地时间失败','请联系管理员风哥')
            time.sleep(5)
            sys.exit(app.exec_())









    
    #设定关闭确认框
    def closeEvent(self, event):
        reply = QMessageBox.question(self,  '退出选项',  '你确定要退出吗？',  QMessageBox.Yes | QMessageBox.No,  QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    @pyqtSlot()
    def on_export_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionleave_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionexit_triggered(self):
        """
        Slot documentation goes here.
        """
        reply = QMessageBox.question(self,  '退出选项',  '你确定要退出吗？', QMessageBox.Yes | QMessageBox.No,  QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass

    #新员工入职
    @pyqtSlot()
    def on_action_xinyuangong_triggered(self):
        """
        Slot documentation goes here.
        """
        #新员工界面先打开，用exec_()方法来执行调用
        app = Dialog()
        app.exec_()
        #到这里，就调用了新员工入职窗口，‘提交’的信息直接在
        # dialog里完成，信息直接被提交到mysql table empl
        # oyee里，同时当期的table‘工资表’增加一行，提交成
        # 功则提示成功，失败就说联系风哥。
        
    #
       
    
    #     cursor=db.cursor
    #
    #     #table employee格式提示:
    #     #varchar/varchar/varchar
    #     #datetime/datetime
    #     #int/int
    #     sql = "insert into employee(" \
    #           "Name, Count, Id, " \
    #           "InTime, OutTime," \
    #           "BasicWeeklySalary, Basic4WeeksSalary)" \
    #           "values(%s, %s, %s," \
    #           "%s, %s," \
    #           "%d, %d)"
    #
    #     cursor.execute(sql%(Name, Count, Id,
    #                         InTime, OutTime,
    #                         BasicWeeklySalary, Basic4WeeksSalary))
              
        


    #离职
    @pyqtSlot()
    def on_actionleave_2_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionchange_info_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionabout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(self, '帮助', '快快快实现')

    
    @pyqtSlot()
    def on_actionhelp_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(self,'帮助','没啥好帮的')

    @pyqtSlot()
    def on_pushButton_timeEnsure_clicked(self):
        """
        Slot documentation goes here.
        """
        _time_ensure = str(self.dateEdit.dateTime()).replace(' ', '')[23:-1]
        print(_time_ensure)
        _time_ensure = '%s,0'%_time_ensure
        print(_time_ensure)
        full_time = _time_ensure.split(',')
        print (full_time)
        
        ensure_time = "%s-%s-%s 00:00:00"%(full_time[0], 
        full_time[1], full_time[2])
        print(ensure_time)

    
    #提交表单按钮，只有所有人发放工资后才能提交！
    @pyqtSlot()
    def on_pushButton_submint_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
        
        
        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()


    sys.exit(app.exec_())
    
