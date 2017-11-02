# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5 import QtWidgets

from Mysql_app import *


from Ui__new_employee import Ui_Dialog


import sys




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

        #自动获取max_id的值，作ID
        try:    #用try来解决第一个用户的问题

            self.lineEdit_2.setText(str(max_id()))

        except:

            pass


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

        #添加新员工
        try:
            # if self.lineEdit.text().replace(' ','')=='':
            #     QMessageBox.information(self,'错误提醒','请输入姓名！')
            #
            # else:

            #入职员工cycle
            #从dateEdit里提取时间要计算
            time2str = ChangeQttime2str(self.dateEdit.date())
            DeltaDays_Monday=int(str(arrow.get().date()-next_Monday(time2str)).split(' ')[0])

            if DeltaDays_Monday < 0:

                delta_Weeks = 0

            else:

                delta_Weeks = DeltaDays_Monday/7+1






            Employee.create(
                    id = self.lineEdit_2.text(),
                    Name = self.lineEdit.text(),
                    _Id = self.lineEdit_3.text(),
                    In_Time = self.dateEdit.text(),
                    #OutTime = 'Null'
                    BasicWeeklySalary = self.lineEdit_4.text(),
                    FourWeeklyBonus = self.lineEdit_5.text()
                )


            #给weekly新建人员，
            Weekly.create (
                Check_Friday = last_Friday(),                  #本周五的date
                id = self.lineEdit_2.text(),                           #
                Name = self.lineEdit.text(),
                #WeeklySalary = IntegerField(default=350),      #周薪
                #FourWeeklyBonus = IntegerField(default=2000),  #四周新
                Cycle = delta_Weeks,
                #Rights = FloatField(default=100000),
                #Fee = FloatField(default=0),
                #Cut = FloatField(default=0),
                #Remark = CharField(default='扣款细则：'),
                #RealPay = FloatField(default=0)
            )





            QMessageBox.information(self,'创建成功','创建新员工成功！')

        except:

            QMessageBox.information(self, '失败提醒',
                                    '创建新员工失败,请检查网络，然后联系风哥！')
            sys.exit(app.exec_())








        # 笨方法初始化界面，一个个清除
        self.lineEdit.setText('')             # 清除姓名
        self.lineEdit_2.setText('800')        # 初始化账号，即员工编号
        self.lineEdit_3.setText('')           # 初始化身份证
        # 这里再次获得新的id值，然后填入新的格子里，为下一个新员工做准备

        self.lineEdit_2.setText(str(max_id()))









        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())

