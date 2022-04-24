# coding:utf-8
# pyqt5_24时间(QDateTimeEdit)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,QDateTime,QTimer,Qt

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.lay = QVBoxLayout()
        self.set_main()
        self.resize(300,200)
        self.setWindowTitle("pyqt5_24时间(QDateTimeEdit)")
        self.setLayout(self.lay)
    '''
        弹出日历设置日期时间
    '''
    def set_main(self):
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(),self)     # 创建日期时间控件
        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")               # 设置时间显示格式，年(yyyy) 月(MM) 日(dd) 时(HH) 分(mm) 秒(ss)
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))     # 设置最小日期，当前日期后退365天
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))      # 设置最大日期，当期日期前进365天
        self.dateEdit.setCalendarPopup(True)                                # 允许弹出日历控件
        self.dateEdit.dateChanged.connect(self.Date_change)
        self.dateEdit.dateTimeChanged.connect(self.Date_Time_change)
        self.dateEdit.timeChanged.connect(self.Time_change)
        # 创建按键用于获取日期和时间
        self.bt = QPushButton("获取日期和时间")
        self.bt.clicked.connect(self.get_time)
        self.bt1 = QPushButton("实时显示时间")
        self.bt1.clicked.connect(self.show_time)
        # 布局
        self.lay.addWidget(self.dateEdit)
        self.lay.addWidget(self.bt)
        self.lay.addWidget(self.bt1)
    '''日期改变触发函数'''
    def Date_change(self,date):
        print(date)
    '''日期或者时间发生改变时触发函数'''
    def Date_Time_change(self,dateTime):
        print(dateTime)
    '''时间发生改变时执行'''
    def Time_change(self,time):
        print(time)
    '''按钮获取时间日期'''
    def get_time(self):
        # 获取时间日期
        dateTime = self.dateEdit.dateTime()
        # 获取最大日期
        maxDate = self.dateEdit.maximumDate()
        # 获取最大日期时间
        maxDateTime = self.dateEdit.maximumDateTime()
        # 获取最大时间
        maxTime = self.dateEdit.maximumTime()
        # 获取最小日期
        minDate = self.dateEdit.minimumDate()
        # 获取最小日期时间
        minDateTime = self.dateEdit.minimumDateTime()
        # 获取最小时间
        minTime = self.dateEdit.minimumTime()
        '''终端输出时间'''
        print("\n选择日期时间")
        print("日期时间=%s" % str(dateTime))
        print('最大日期=%s' % str(maxDate))
        print('最大日期时间=%s'  % str(maxDateTime))
        print('最大时间=%s' % str(maxTime))
        print('最小日期=%s' % str(minDate))
        print('最小日期时间=%s' % str(minDateTime))
        print('最小时间=%s' % str(minTime))
    
    """
        使用Qtimer定时器实时显示时间
    """
    def show_time(self):
        dialog = QDialog()
        dialog.resize(300,200)
        dialog.setWindowTitle("实时显示时间")
        lable = QLabel("实时显示时间")        # 用于显示时间
        button1 = QPushButton("开始")        # 按钮开始输出显示时间
        button2 = QPushButton("结束")        # 停止
        # 创建网格布局
        lay = QGridLayout()
        # Qt中的定时器函数
        timer = QTimer()
        # 定时器溢出关联函数
        timer.timeout.connect(lambda:self.showtime(lable))
        lay.addWidget(lable,0,0,1,2)
        lable.setAlignment(Qt.AlignCenter)
        lay.addWidget(button1,1,0)
        lay.addWidget(button2,1,1)
        # 开始显示时间
        button1.clicked.connect(lambda:self.starttimer(timer,button1,button2))
        # 停止显示时间
        button2.clicked.connect(lambda:self.endtimer(timer,button1,button2,dialog))
        dialog.setLayout(lay)
        dialog.setWindowModality(Qt.NonModal)   # 应用程序模态，阻止和任何其他窗口进行交互
        dialog.exec_()                          # 保持对话窗口显示
        
    # 定时捕捉时间并更新
    def showtime(self,lable):
        time = QDateTime.currentDateTime()                        # 获取当前时间
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")   # 设置时间显示格式
        print(timedisplay)
        lable.setText(timedisplay)
    # 打开定时器
    def starttimer(self,timer,button1,button2):
        # 每隔一秒刷新一次，这里设置为1000ms即1s
        timer.start(1000)
        button1.setEnabled(False)      # 不允许点击
        button2.setEnabled(True)       # 允许点击
    # 关闭定时器
    def endtimer(self,timer,button1,button2,dialog):
        timer.stop()
        button1.setEnabled(True)
        button2.setEnabled(False)
        dialog.close()
        
# 主函数
if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    # 创建窗口
    GUI = UI()
    # 显示
    GUI.show()
    sys.exit(app.exec_())