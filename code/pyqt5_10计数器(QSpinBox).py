# coding:utf-8
# pyqt5_10计数器(QSpinBox)
# author：Qinyuan

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UI(QWidget):
    def __init__(self):
        super().__init__()
        # 水平布局
        self.lay = QHBoxLayout()
        self.lay1 = QHBoxLayout()
        # 垂直布局
        self.mainlay = QVBoxLayout()
        # 创建盒子用于输入两个求和的值
        self.add_box = QGroupBox("请输入两个整数求和")
        self.add_box.setFlat(False)
        self.result_box = QGroupBox("求和结果")
        self.result_box.setFlat(False)
        # 创建窗口
        self.set()
        self.setLayout(self.mainlay)
        # 设置窗口标题
        self.setWindowTitle("pyqt5_10计数器(QSpinBox)")
        self.resize(300,200)
        
    def set(self):
        # 创建两个计数框
        num1 = QSpinBox()
        num1.setRange(0,1000000)   # 设置范围
        num1.setSingleStep(1)      # 设置步长
        num1.setValue(0)           # 设置初始值
        
        num2 = QSpinBox()
        num2.setRange(0,1000000)   # 设置范围
        num2.setSingleStep(1)      # 设置步长
        num2.setValue(0)           # 设置初始值
        
        # 创建文本控件显示求和值
        result = QLineEdit()
        result.setAlignment(Qt.AlignCenter)
        result.setReadOnly(True)
        result.setFont(QFont("KaiTi",10))
        
        # 关联函数
        num1.valueChanged.connect(lambda:self.fun(num1,num2,result))
        num2.valueChanged.connect(lambda:self.fun(num1,num2,result))
        
        # 添加到布局中
        self.lay.addWidget(num1)
        self.lay.addWidget(num2)
        self.lay1.addWidget(result)
        self.add_box.setLayout(self.lay)
        self.result_box.setLayout(self.lay1)
        self.mainlay.addWidget(self.add_box)
        self.mainlay.addWidget(self.result_box)
    
    # 关联函数求和
    def fun(self,num1,num2,result):
        data = str(num1.value()) + " + " + str(num2.value()) + " = " + str(num1.value() + num2.value())
        result.setText(data)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(r"PyQt5\ICO\test.ico"))
    GUI = UI()
    GUI.show()
    sys.exit(app.exec_())