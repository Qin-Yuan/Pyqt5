# coding:utf-8
# pyqt5_09按钮(QComboBox)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口标题
        self.setWindowTitle("pyqt5_09按钮(QComboBox)")
        self.resize(300,300)
        # 垂直布局
        self.lay = QVBoxLayout()
        # 执行set()函数
        self.set()
        # 窗口布局
        self.setLayout(self.lay)
    
    # 创建下拉列表框
    def set(self):
        # 创建 QComboBox 下拉列表框
        cb = QComboBox()
        # 添加下拉选项
        cb.addItem("C")
        cb.addItem("JAVA")
        cb.addItem("Python")
        cb.addItem("C++")
        # 一次添加多个
        cb.addItems(["C#","PHP","JavaScript"])
        # 当下拉选项的索引号发生改变时触发信号 
        cb.currentIndexChanged.connect(lambda:self.do(cb))
        self.lay.addWidget(cb)
        
    # 关联函数
    def do(self,cb):
        print("索引号%s ：%s" % (cb.currentIndex(),cb.currentText()))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())