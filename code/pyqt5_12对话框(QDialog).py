# coding:utf-8
# pyqt5_12对话框(QDialog)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_12对话框(QDialog)")
        self.resize(300,100)
        self.set_button()
        
    '''为主窗口创建按钮类控件'''
    def set_button(self):
        self.bt = QPushButton("对话框测试",self)         # 为主窗口创建按键
        self.bt1 = QPushButton("退出",self)             # 为主窗口创建按键
        self.bt.move(50,30)                             # 移动按钮的位置
        self.bt1.move(150,30)                           # 移动按钮的位置
        self.bt.clicked.connect(self.set_dialog)        # 按钮点击链接函数set_dialog
        self.bt1.clicked.connect(self.close)       # 按钮点击链接函数set_dialog
    
    '''按钮点击触发函数，弹出对话框'''
    def set_dialog(self):
        dialog = QDialog()                                  # 创建对话框
        bt = QPushButton("关闭窗口",dialog)                  # 为dialog窗口创建按钮
        bt.clicked.connect(lambda:self.close_UI(dialog))    # 关联关闭窗口程序
        bt1 = QPushButton("打开新对话框",dialog)             # 为dialog窗口创建按钮
        bt1.clicked.connect(self.set_dialog)
        bt.move(50,100)
        bt1.move(50,50)
        dialog.setWindowTitle("对话框")          # 设置弹出对话框的标题
        dialog.setWindowModality(Qt.NonModal)   # 应用程序模态，阻止和任何其他窗口进行交互
        dialog.exec_()                          # 保持对话窗口显示
    
    '''关闭窗口'''
    def close_UI(self,ui):
        ui.close()
        
    '''关闭程序'''
    def close(self):
        sys.exit()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())
    