# coding:utf-8
# pyqt5_23日历(QCalendar)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate,Qt

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.lay = QVBoxLayout()
        self.set_main()
        self.resize(300,300)
        self.setWindowTitle("pyqt5_23日历(QCalendar)")
        self.setLayout(self.lay)
    # 主窗口初始化
    def set_main(self):
        date = QCalendarWidget()
        date.setMinimumDate(QDate(1978,7,8))    # 设置最小日期
        date.setMaximumDate(QDate(2050,7,8))    # 设置最大日期
        date.setGridVisible(True)               # 设置显示格网
        # 窗口选定一个日期后会触发关联函数更新lab显示，发送QDate信号
        date.clicked[QDate].connect(self.showDate)
        self.lab = QLabel()
        dat = date.selectedDate()
        # 设置文本框显示的格式
        self.lab.setText(dat.toString("yyyy-MM-dd dddd"))
        #self.lab.move(20,300)
        self.lay.addWidget(date,alignment=Qt.AlignCenter)
        self.lay.addWidget(self.lab,alignment=Qt.AlignCenter)
    # 显示日期
    def showDate(self,dat):
        self.lab.setText(dat.toString("yyyy-MM-dd dddd"))
        
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