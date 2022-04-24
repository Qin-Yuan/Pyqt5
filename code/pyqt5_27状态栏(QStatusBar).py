# coding:utf-8
# pyqt5_27状态栏(QStatusBar)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_set()
        self.setWindowTitle("pyqt5_27状态栏(QStatusBar)")
        self.resize(500,300)
    # 状态栏创建函数
    def main_set(self):
        bar = self.menuBar()        # 创建一个菜单栏
        file = bar.addMenu("文件")  # 新建一个下拉列表
        file.addAction("新建")
        file.addAction("打开")
        file.addAction("保存")
        file.triggered[QAction].connect(self.do)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()         # 创建一个状态栏
        self.setStatusBar(self.statusBar)     # 布局状态栏
    # 信号处理函数
        # 点击处理函数
    def do(self,a):
        if a.text() == "新建":
            self.statusBar.showMessage(a.text(),3000)  # 设置状态栏的信息文字
            print("新建文件")
        elif a.text() == "打开":
            self.statusBar.showMessage(a.text(),3000)
            print("打开文件")
        elif a.text() == "保存":
            self.statusBar.showMessage(a.text(),3000)
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