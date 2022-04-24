# coding:utf-8
# pyqt5_26工具栏(QToolBar)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_set()
        self.setWindowTitle("pyqt5_26工具栏(QToolBar)")
        self.resize(500,300)
    # 功能按键创建函数 
    def main_set(self):
        tb = self.addToolBar("file")   # 创建一个工具栏图标条
        new = QAction(QIcon(r"PyQt5\ICO\新建.ico"),"NEW",self)
        open =  QAction(QIcon(r"PyQt5\ICO\打开文件.ico"),"OPEN",self)
        save = QAction(QIcon(r"PyQt5\ICO\保存.ico"),"SAVE",self)
        tb.addAction(new)
        tb.addAction(open)
        tb.addAction(save)
        tb.actionTriggered.connect(self.do)
    # 点击处理函数
    def do(self,a):
        if a.text() == "NEW":
            print("新建文件")
        elif a.text() == "OPEN":
            print("打开文件")
        elif a.text() == "SAVE":
            print("保存文件")
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