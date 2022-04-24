# coding:utf-8
# pyqt5_15对话框(QFontDialog)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_15对话框(QFontDialog)")
        self.lay = QVBoxLayout()  # 创建垂直布局框
        self.resize(300,300)
        self.set_main()           # 运行主窗口设置函数
        self.setLayout(self.lay)  # 设置主窗口的布局
        
    '''按钮设置字体'''
    def set_main(self):
        bt = QPushButton("字体设置")       # 字体设置按钮
        text = QLabel("覃原学PyQt5!")      # 文本框测试
        self.lay.addWidget(bt,alignment=Qt.AlignCenter)
        self.lay.addWidget(text,alignment=Qt.AlignCenter)
        bt.clicked.connect(lambda:self.set_text(text))
    
    '''设置字体'''
    def set_text(self,text):
        # 弹出字体选择对话框，提供用户设置字体,font为用户设置的返回值
        font , ok = QFontDialog.getFont()
        if ok:
            text.setFont(font)    # 设置字体
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())