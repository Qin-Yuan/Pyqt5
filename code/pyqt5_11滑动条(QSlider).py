# coding:utf-8
# pyqt5_11滑动条(QSlider)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        # 垂直布局
        self.lay = QVBoxLayout()
        # 执行创建函数
        self.set()
        # 布局
        self.setLayout(self.lay)
        self.resize(300,100)
        # 设置窗口标题
        self.setWindowTitle("pyqt5_11滑动条(QSlider)")
        
    # 创建控件
    def set(self):
        # 创建水平滑动条
        sl = QSlider(Qt.Horizontal)
        # 设置范围、步值等参数
        sl.setMinimum(1)       # 设置最小值
        sl.setMaximum(100)     # 设置最大值
        sl.setSingleStep(1)    # 设置步长
        sl.setValue(0)         # 设置当前值
        sl.setTickInterval(10) # 设置刻度间隔
        sl.setTickPosition(QSlider.TicksAbove)  # 在水平滑块下方
        
        # 创建显示文字内容
        text = QLabel("覃原学pyqt5!")
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QFont("KaiTi",10))
        
        # 滑块值发生改变时触发
        sl.valueChanged.connect(lambda:self.func(sl,text))
        
        # 添加到布局中
        self.lay.addWidget(text)
        self.lay.addWidget(sl)
        
    # 功能执行函数
    def func(self,sl,text):
        # 获取 sl 的值作为设置 text 字体的大小
        size = sl.value()
        # 设置 text 文本的字体和大小
        text.setFont(QFont("KaiTi",size))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())