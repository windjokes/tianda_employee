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



from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,  QMessageBox, QTableWidgetItem
from PyQt5 import QtWidgets

import time
import sys
from app import *


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

        # 初始化先获取weekly的表单填入当天
        # 对于表单日期做判断，录入当期表单

        data_sql=Weekly.select().where(Weekly.ThisFridayDate ==last_Friday())
        data = []
        row_count = 0
        for i in data_sql:
            l=()
            l=(i.id,i.Name,i.Rights,i.Fee,i.Cut,i.Remark,i.RealPay)
            data.append(l)
            row_count +=1
            #print(l,type(l[0]))  #(800831, '150216', 100000.0, 0.0, 0.0, '扣款细则：', 0.0) <class 'tuple'>
        self.tableWidget_thisweek.setRowCount(row_count)
        for i in range(0,row_count):
            for j in range(0,7):
                data_box = data[i][j]
                if data_box != str:
                    data_box = str(data_box)
                newItem = QTableWidgetItem(data_box)
                self.tableWidget_thisweek.setItem(i, j,newItem )


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
        reply = QMessageBox.question(self,  '退出选项',  '你确定要退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,  QMessageBox.No)
        
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
        # oyee里，同时当期的table‘weekly’增加一行，提交成
        # 功则提示成功，失败就说联系风哥。

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

    #查询时间，查询模块晚点来搞
    @pyqtSlot()
    def on_pushButton_timeEnsure_clicked(self):
        """
        Slot documentation goes here.
        """
        _time_ensure = str(self.dateEdit.dateTime()).replace(' ', '')[23:-5]
        print(_time_ensure)


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
    
