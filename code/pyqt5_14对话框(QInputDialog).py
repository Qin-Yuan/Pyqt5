# coding:utf-8
# pyqt5_14对话框(QInputDialog)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_14对话框(QInputDialog)")
        self.lay = QFormLayout()        # 表单布局
        self.set_main()                 # 主窗口
        self.setLayout(self.lay)        
    
    '''主窗口布局'''
    def set_main(self):
        bt1 = QPushButton("列表选项")       # 普通按键按钮
        bt1.clicked.connect(self.get_item)  # 关联对话弹出框
        self.lab1 = QLineEdit()             # 文本框
        self.lab1.setReadOnly(True)         # 设置为只显示，不能输入
        self.lay.addRow(bt1,self.lab1)      # 水平添加到表单布局中
        
        bt2 = QPushButton("获得字符串")
        bt2.clicked.connect(self.get_Text)
        self.lab2 = QLineEdit()
        self.lab2.setReadOnly(True)
        self.lay.addRow(bt2,self.lab2)
        
        bt3 = QPushButton("获得整数")
        bt3.clicked.connect(self.get_Int)
        self.lab3 = QLineEdit()
        self.lab3.setReadOnly(True)
        self.lay.addRow(bt3,self.lab3)
        
    '''获取列表值'''
    def get_item(self):
        items = ("选择一","选择二","选择三","选择四")
        # 弹出选择对话框，返回选中的值和是否成功
        item , ok =QInputDialog.getItem(
                                        self,
                                        "列表选择", # 列表窗口标题
                                        "可选项",   # 提示
                                        items,     # 列表选项 
                                        0,         # 默认选项索引号0
                                        False)     # 不允许在文本框中输入
        # 判断是否设置成功，设置主窗口文本框的值
        if ok and item:
            self.lab1.setText(item)
    
    '''文本框输入'''
    def get_Text(self):
        text,ok = QInputDialog.getText(
                                        self,
                                        "字符串输入",
                                        "请输入字符串"
                                        )
        if  text and ok :
            self.lab2.setText(text)
    
    '''整数输入'''
    def get_Int(self):
        num , ok =QInputDialog.getInt(self,"数字输入","请输入数字")
        if ok :
            # 注意这里num是int型，而setText输入的必须是str型，需要转换
            self.lab3.setText(str(num))
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())