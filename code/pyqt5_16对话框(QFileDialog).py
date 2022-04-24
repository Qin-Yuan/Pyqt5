# coding:utf-8
# pyqt5_16对话框(QFileDialog)
# author：Qinyuan

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyqt5_16对话框(QFileDialog)")
        self.lay = QFormLayout()
        self.set_main()
        self.setLayout(self.lay)
    
    '''主窗口设置，一个文件游览，一个用于显示文件的QLabel'''
    def set_main(self):
        # 用于显示图片
        self.pic = QLabel()
        # 用于显示文本,设置为只读模式
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        # 一个打开文本，一个打开图片的按钮
        bt_pic = QPushButton("打开图片")
        bt_pic.clicked.connect(self.get_pic)
        bt_text = QPushButton("打开文本")
        bt_text.clicked.connect(self.get_text)
        self.lay.addRow(bt_pic,bt_text)
        self.lay.addRow(self.pic)
        self.lay.addRow(self.text)
        
    '''打开图片'''
    def get_pic(self):
        # 弹出对话框，返回用户选择的路径
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件',r'PyQt5\ICO',"Image files(*.jpg *.png *.ico)")
        # 将QLabel设置成图片
        self.pic.setPixmap(QPixmap(fname))
    '''打开文本文件'''
    def get_text(self):
        # 弹出文件选择对话框
        file = QFileDialog()
        # 设置游览文件为所有类型
        file.setFileMode(QFileDialog.AnyFile)
        # 设置过滤器
        file.setFilter(QDir.Files)
        if file.exec_():
            # 查询文件
            filenames = file.selectedFiles()
            # ‘utf-8’格式读取文件，设计中文
            with open(filenames[0],'r',encoding='utf-8') as f:
                data = f.read()
                self.text.setText(data)
                
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