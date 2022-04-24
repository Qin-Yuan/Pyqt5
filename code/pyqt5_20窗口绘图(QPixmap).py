# coding:utf-8
# pyqt5_20窗口绘图(QPixmap)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_20窗口绘图(QPixmap)")
        self.lay = QVBoxLayout()
        self.set_main()
        self.setLayout(self.lay)
        self.resize(300,300)
    
    # 图像路径获取
    def set_main(self):
        self.pic = QLabel()                 # 创建图片显示文本框
        self.pic.setAlignment(Qt.AlignCenter)
        bt = QPushButton("选择打开的图片")
        bt.clicked.connect(self.get_pic)    #  关联获取显示图像函数
        self.lay.addWidget(bt,alignment=Qt.AlignLeft)
        self.lay.addWidget(self.pic)
        
    '''打开图片'''
    def get_pic(self):
        # 弹出对话框，返回用户选择的路径
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件',r'PyQt5',"Image files(*.jpg *.png *.ico)")
        # 将QLabel设置成图片
        self.pic.setPixmap(QPixmap(fname))
        
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