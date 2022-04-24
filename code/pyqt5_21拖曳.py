# coding:utf-8
# pyqt5_21拖曳
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 创建拖曳处理控件,这里继承QComboBox下拉列表类
class Combo(QComboBox):
    def __init__(self,title,parent):
        super(Combo,self).__init__(parent)
        # 允许拖曳插入
        self.setAcceptDrops(True)
    '''当鼠标进入该控件时触发，并判断是否有有效数据传入'''
    def dragEnterEvent(self,e):
        # 检测是否有文本
        if e.mimeData().hasText():
            # 连接允许
            e.accept()
        else:
            # 忽视拖曳
            e.ignore()
    '''当拖曳操作在目标控件上被释放时，这个事件将被触发'''
    def dropEvent(self,e):
        self.addItem(e.mimeData().text())
# 主窗口
class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_21拖曳")
        self.resize(200,200)
        self.set_main()
    '''主窗口初始化函数'''
    def set_main(self):
        # 创建表格布局
        lay = QFormLayout()
        lay.addRow(QLabel("拖曳文本框中的数据到下拉列表中"))
        #  创建文本输入框
        edit = QLineEdit()
        # 设置允许拖曳
        edit.setDragEnabled(True)
        # 创建一个下拉列表，允许拖曳插入
        com = Combo("Button",self)
        lay.addRow(edit)
        lay.addRow(com)
        self.setLayout(lay)
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