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
from PyQt5.QtWidgets import QMainWindow,  QMessageBox, QTableWidgetItem,QDialog
from PyQt5 import QtWidgets

import time
import sys
from Mysql_app import *
import arrow


from Ui_employee import Ui_MainWindow
from Ui__new_employee import Ui_Dialog







changed_row = 1
changed_column = 1





#
# class RealPay_Calculate(object):
#
#     def __init__(self):
#         self.
#
#     #根据状态来调用呗
#     def States0(self):
#         pass
#
#
#     def States123(self):
#         pass
#
#     def States4(self):
#         pass


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
    def on_pushButton_clicked(self,event):
        """
        Slot documentation goes here.
        """
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


            #给表格加一行
            row_count = ui.tableWidget_thisweek.rowCount()
            ui.tableWidget_thisweek.insertRow(row_count)

            #读取数据
            data_sql=Weekly.select().where(Weekly.id ==self.lineEdit_2.text())

            for i in data_sql:

                l=[i.Cycle,i.id,i.Name,i.Rights,i.Fee,i.Cut,
                   i.Remark,i.CheckRights,i.CheckFee,i.CheckPay]

            #循环入数据
            for i in range(0,10):
                print (l[i])
                if l[i] !=str:
                    l[i] = str(l[i])
                newItem = QTableWidgetItem(l[i])
                ui.tableWidget_thisweek.setItem(row_count, i, newItem)

            #在行里面加入控件
            CheckBox = QtWidgets.QComboBox()
            CheckBox.addItem('未完成')
            CheckBox.addItem('完成')
            self.tableWidget_thisweek.setCellWidget(row_count,10,CheckBox)


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

        #从服务器数据表提取信息
        data_sql=Weekly.select().where(Weekly.Check_Friday ==last_Friday())
        #先把前面10列从数据表搞出来
        data = []
        row_count = 0
        for i in data_sql:
            l=()
            l=(i.Cycle,i.id,i.Name,i.Rights,i.Fee,i.Cut,
               i.Remark,i.CheckRights,i.CheckFee,i.CheckPay)
            data.append(l)
            row_count +=1
            #print(l,type(l[0]))  #(800831, '150216', 100000.0, 0.0, 0.0, '扣款细则：', 0.0) <class 'tuple'>

        self.tableWidget_thisweek.setRowCount(row_count)


        #一次性全部循环进去
        for i in range(0,row_count):
            for j in range(0,10):

                #给前10列添加数据
                data_box = data[i][j]

                if data_box != str:
                    data_box = str(data_box)
                newItem = QTableWidgetItem(data_box)
                self.tableWidget_thisweek.setItem(i, j,newItem )



            #给第11列添加QCOMBOBOX
            CheckBox = QtWidgets.QComboBox()
            CheckBox.addItem('未完成')
            CheckBox.addItem('完成')
            self.tableWidget_thisweek.setCellWidget(i,10,CheckBox)

            #算出cycle





        #入职时间抓取，用于计算新员工，哎，烦



        #
        # for i in range(0,row_count):


        #发放列生成QComboBox下拉




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
        new_employee = Dialog()
        new_employee.exec_()


    @pyqtSlot()
    def on_newbee_clicked(self):
        """
        Slot documentation goes here.
        """
        new_employee = Dialog()
        new_employee.exec_()


    #离职
    @pyqtSlot()
    def on_actionleave_2_triggered(self):
        """
        Slot documentation goes here.
        """
        pass


    @pyqtSlot()
    def on_beeleave_clicked(self):
        """
        Slot documentation goes here.
        """
        pass


    
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
        time_test = ChangeQttime2str(self.dateEdit.date())
        print(time_test)



    #提交表单按钮，只有所有人发放工资后才能提交！
    @pyqtSlot()
    def on_pushButton_submint_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError



    #item CheckPay同步运算
    #取出改变的内容-。-似乎没有必要
    @pyqtSlot(QTableWidgetItem)
    def on_tableWidget_thisweek_itemChanged(self, item):
        """
            Slot documentation goes here.

            @param item DESCRIPTION
            @type QTableWidgetItem
        """
            # QMessageBox.information(self,'good','good')
            # 载入界面就开始出来一堆Box
            # 我草！！这个才是正宗啊！
        global changed_item_content

        try:

            changed_item_content = item.text()

        except:

            pass



    #item CheckPay同步运算
    @pyqtSlot(int, int)
    def on_tableWidget_thisweek_cellChanged(self, row, column):
        """
                        Slot documentation goes here.

                        @param row DESCRIPTION
                        @type int
                        @param column DESCRIPTION
                        @type int
        """

        newItem = QTableWidgetItem('23')
        #下面是工资的算法：

        if column == 3 or column ==4 or column ==5:

            #这边用try来解决加载时候，item里面是nonetype的问题
            try:

                # 不管是哪个row，反正就是取它column的值，然后再算一遍
                # ColumnNum_345 = int(float(changed_item_content))
                #取周期
                CycleNum = int(self.tableWidget_thisweek.item(row,0).text())
                #动态权益
                RightsNum = int(float(self.tableWidget_thisweek.item(row,3).text()))
                #扣款
                CutNum = int(float(self.tableWidget_thisweek.item(row,5).text()))
                #手续费
                FeeNum = int(float(self.tableWidget_thisweek.item(row,4).text()))
                #留存4周奖金
                CheckRights = int(float(self.tableWidget_thisweek.item(row,7).text()))
                #留存手续费
                CheckFee = int(float(self.tableWidget_thisweek.item(row,7).text()))
                #入职时间转化为天数
                DeltaDays = int(str(this_Friday(self.tableWidget_thisweek.item(row,11))-arrow.get().date()).split(' ')[0])



                #判断cycle,从而给工资定0or123or4
                if CycleNum == 0:

                    FinalSalary = 350 - DeltaDays*70
                    newItem = QTableWidgetItem(str(FinalSalary))
                    self.tableWidget_thisweek.setItem(row,9,newItem)
                    print('1')

                elif CycleNum%4 != 0:
                    if FeeNum<=450:

                        FinalSalary = 350-CutNum

                    else:

                        FinalSalary = 350-CutNum-FeeNum

                    newItem = QTableWidgetItem(str(FinalSalary))
                    self.tableWidget_thisweek.setItem(row,9,newItem)

                else:

                    FinalSalary =CheckRights-CutNum+350

                    print('3')


            except:

                pass












        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()



    sys.exit(app.exec_())
    

