# coding:utf-8
# pyqt5_22剪贴板(QClipboard)
# author：Qinyuan

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QIcon

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.lay = QGridLayout()
        self.set_main()
        self.setLayout(self.lay)
        self.resize(300,300)
        self.setWindowTitle("pyqt5_22剪贴板(QClipboard)")
        
    def set_main(self):
        # 按钮
        copy_text = QPushButton("&Copy Text")
        paste_text = QPushButton("Paste &Text")
        copy_image = QPushButton("Co&py Image")
        paste_image = QPushButton("Paste &Image")
        self.lay.addWidget(copy_text,0,0)
        self.lay.addWidget(copy_image,0,1)
        self.lay.addWidget(paste_text,1,0)
        self.lay.addWidget(paste_image,1,1)
        # QLable文本框
        edit = QLineEdit()
        text = QLabel("覃原学pyqt5!")
        image = QLabel()
        image.setPixmap(QPixmap(r"PyQt5\ICO\eason.ico"))
        self.lay.addWidget(edit,2,0,)
        self.lay.addWidget(text,3,0)
        self.lay.addWidget(image,4,0)
        # 按键关联函数
        copy_text.clicked.connect(lambda:self.copy_text(edit))
        paste_text.clicked.connect(lambda:self.paste_text(text))
        copy_image.clicked.connect(self.copy_image)
        paste_image.clicked.connect(lambda:self.paste_image(image))
    
    '''文本复制方法'''
    def copy_text(self,edit):
        # 实例化cliphoard，剪贴板
        cliphoard = QApplication.clipboard()
        # 设置剪贴板的内容
        cliphoard.setText(edit.text())
    '''粘贴文本方法'''
    def paste_text(self,text):
        # 实例化cliphoard，剪贴板
        cliphoard = QApplication.clipboard()
        # 设置文本框的数据
        text.setText(cliphoard.text())
    '''图片复制方法'''
    def copy_image(self):
        # 弹出对话框，返回用户选择的路径
        fname,_ = QFileDialog.getOpenFileName(self,'打开文件',r'PyQt5\ICO',"Image files(*.jpg *.png *.ico)")
        # 实例化粘贴板
        cliphoard = QApplication.clipboard()
        cliphoard.setPixmap(QPixmap(fname))
    '''图片粘贴'''
    def paste_image(self,image):
        cliphoard = QApplication.clipboard()
        image.setPixmap(cliphoard.pixmap())
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